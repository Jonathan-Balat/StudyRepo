/* Servo_ctrl

 modified July 23 2023
 by Jonathan Balat
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 90;    // variable to store the servo position
int pos_tmp = 0;    // variable to store the servo reference position used as return point
int sweep_dir = 0; // 0 right, 1 left
int scan_rate = 15; // Arbitrary default value
int stat_continuous = 0;
int stat_once = 0;

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object

  // Start Serial
  Serial.begin(9600);
  
}

void loop() 
{
  if(stat_once)
  {
    servo_sweep_once();
  }
  else if (stat_continuous)
  {
    servo_sweep_continuous();  
  }
  else
  {
    
  }
}


/* SERIAL-PARSE FUNCTIONS */
void serialEvent()
{
  int state   = 0;
  int action  = -1;
  int command = -1;
  int value   = -1;
  char sig_char = ' ';

  while (Serial.available())
  {
    sig_char = Serial.read();
    if ((sig_char == '[') and (state==0))
    {
      action = Serial.parseInt();
      state = 1;
    }
    else if (state==1)
    {
      command = Serial.parseInt();
      state = 2;
    }
    else if (state==2)
    {
      value = Serial.parseInt();
      state = 3;
    }
    else if (state==3)
    {
      Serial.read(); // Discards all other data on buffer
      io_control(action, command, value);
      state = 0;
    }
    else
    {
      // Reads all other WS and characters outside of Frame
    }
  }
}


/********** IO CONTROL **********/
void io_control(int action, int command, int value)
{
  int return_val;
  switch (action)
  {
    case 0:
      return_val = io_set(command, value);
      break;

    case 1:
      return_val = io_get(command);
      break;

    case 2:
      return_val = io_test(command);
      break;

    default:
      return_val = 0xE0;
      break;
  }
  
  Serial.println(return_val);  // Error
}

int io_set(int command, int value)
{
  int return_val = 0;

  switch (command)
  {
    case 0:
      servo_set_pos(value);
      stat_continuous = false;
      stat_once = false;
      break;

    case 1:
      stat_once = (value > 0);
      stat_continuous = false;
      break;

    case 2:
      stat_continuous = (value > 0);
      stat_once = false;
      break;

    case 3:
      scan_rate = value;
      break;
      
    default:
      return_val = 0xE1; // Serial Command Set Error
      break;
  }
  return return_val;
}

int io_get(int command)
{ 
  int return_val = 0;
  switch (command)
  {
    case 0:
      return_val = servo_get_pos();
      break;

    case 1:
      return_val = stat_once;

    case 2:
      return_val = stat_continuous;
      break;

    case 3:
      return_val = scan_rate;
      break;

    default:
      return_val = 0xE2; // Serial Command Get Error
      break;   
  }
  return return_val;
}

int io_test(int command)
{
  int return_val = 0;
  switch (command)
  {
    case 0:
      Serial.println("ACK");
      break;
      
    default:
      return_val = 0xE3; // Serial Command Test Error
      break;
  }
  return return_val;
}


/* SERVO FUNCTIONS */
void servo_sweep_continuous()
{
  if (sweep_dir == 0)
  {
    pos--;
  }
  else
  {
    pos++; 
  }
  
  if ((pos == 0) or (pos == 180))
  {
      sweep_dir = not sweep_dir;
  }
  
  myservo.write(pos);
  delay(scan_rate);
}

void servo_sweep_once()
{
  switch(stat_once)
  {
    case 1:
      pos_tmp = pos;
      stat_once++;
      break;
      
    case 2:
    case 3:
      if (sweep_dir == 0)
      {
        pos--;
      }
      else
      {
        pos++; 
      }
      
      if ((pos == 0) or (pos == 180))
      {
          sweep_dir = not sweep_dir;
          stat_once++;  
      }
    
      myservo.write(pos);
      delay(scan_rate);
      break;
      
    case 4:
      if (sweep_dir == 0)
      {
        pos--;
      }
      else
      {
        pos++;
      }
      
      if (pos == pos_tmp)
      {
        stat_once++;  
      }
    
      myservo.write(pos);
      delay(scan_rate);  
      break;

      default:
      stat_once = 0;
  }
}

void servo_set_pos(int pos_new)
{
  myservo.write(pos_new);
  pos = pos_new;
  delay(scan_rate);
}

int servo_get_pos()
{
  return pos;  
}

int __servo_bound_value(int pos_val)
{
  if (pos_val > 180)
  {
    pos_val = 180;  
  }  
  else if (pos_val < 0)
  {
    pos_val = 0;  
  }
  else
  {
    // Do nothing  
  }
  return pos_val;
}
