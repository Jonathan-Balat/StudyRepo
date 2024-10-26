from random import randint
from math import log

from Activation_Class import ActivationClass


def generate_weights(x_size, y_size, div=100):
    col = []
    for x_idx in range(0, x_size):
        row = []
        for y_idx in range(0, y_size):
            row.append(randint(-100, 100) / div)
        col.append(row)

    print(col)
    assert len(col) == x_size, "Weight dimension X did not match to " + str(x_size)
    assert len(col[0]) == y_size, "Weight dimension Y did not match to " + str(y_size)

    return col


def generate_bias(x_size, y_size, hard_value=None, div=100):
    col = []
    for x_idx in range(0, x_size):
        row = []
        for y_idx in range(0, y_size):
            if hard_value is None:
                row.append(randint(-100, 100) / div)
            else:
                row.append(hard_value)
        col.append(row)

    print(col)
    assert len(col) == 1, "Bias dimension X did not match to " + str(1)
    assert len(col[0]) == y_size, "Bias dimension Y did not match to " + str(y_size)

    return col


def neuron_compute(input_data, weights, bias):
    Act = ActivationClass.sigmoid
    weight_xy = len(weights), len(weights[0])

    Z_col = []
    for weight_x_idx in range(0, weight_xy[0]):
        Z_row = []
        for weight_y_idx in range(0, weight_xy[1]):
            # print("\tW*X", weights[weight_x_idx][weight_y_idx],  input_data, bias)
            Z_row.append((weights[weight_x_idx][weight_y_idx] * input_data) + bias)  # Z = (W^T)X+b
        Z_col.append(Z_row)
    # print("Z=", Z_col)

    Z_xy = len(Z_col), len(Z_col[0])
    A_col = []
    for Z_x_idx in range(0, Z_xy[0]):
        A_row = []
        for Z_y_idx in range(0, Z_xy[1]):
            A_row.append(Act(Z_col[Z_x_idx][Z_y_idx]))
        A_col.append(A_row)
    return A_col


def lf_log_loss(y, p, e=1E-7):
    # print("y, p", y, p)
    return -1 * ((y * log(p + e)) + ((1 - y) * (log(1 - p + e))))


def loss_func(computed, sample):
    computed_xy = len(computed), len(computed[0])  # Same size with sample array

    # print(computed_xy)
    loss_col = []
    for comp_x_idx in range(0, computed_xy[0]):

        loss_row = []
        for comp_y_idx in range(0, computed_xy[1]):
            __tmp = lf_log_loss(computed[comp_x_idx][comp_y_idx], sample[comp_x_idx][comp_y_idx])
            loss_row.append(__tmp)

        loss_row = sum(loss_row) / computed_xy[1]
        loss_col.append(loss_row)

    loss_col = sum(loss_col) / computed_xy[0]
    # print("LOG=", __tmp, "----->", computed[comp_x_idx][comp_y_idx], sample[comp_x_idx][comp_y_idx])
    return loss_col


def forward_propagation(data_input, data_output, weights, bias):
    result = []
    for data_idx, input_data in enumerate(data_input):
        input_data_xy = len(input_data), len(input_data[0])

        error_col = []
        for input_x_idx in range(0, input_data_xy[0]):
            error_row = []
            for input_y_idx in range(0, input_data_xy[1]):
                ret_y = neuron_compute(input_data[input_x_idx][input_y_idx], weights, bias[input_x_idx][input_y_idx])
                assert len(ret_y) == 1, "f(x) dimension X did not match to " + str(1)
                assert len(ret_y[0]) == weight_dim[1], "f(x) dimension Y did not match to " + str(weight_dim[1])

                error_row.append(loss_func(ret_y, data_output[data_idx]))
            error_col.append(error_row)
        result.append(error_col)

    print("RESULT=", result)
    assert len(result) == len(data_input), "Result count did not match to Sample count " + str(data_input)
    assert len(result[0]) == len(data_input[0]), "Result dimension X did not match to Sample dimension X" + str(
        data_input[0])
    assert len(result[0][0]) == len(data_input[0][0]), "Result dimension Y did not match to Sample dimension Y" + str(
        data_input[0][0])

    return result


# ######################################### BACK PROPAGATION #########################################
# def update_param(weights, bias, y_arr, p_arr, x_new, alpha=0.001):
# # def update_params(b, w, y, p, x_new, alpha=0.001):
#
#     y_arr_xy = len(y_arr), len(y_arr[0])
#     p_arr_xy = len(p_arr), len(p_arr[0])
#     weights_xy = len(weights), len(weights[0])
#
#     dW_col = []
#     for y_arr_x_idx in range(0, y_arr_xy[0]):
#         dW_row = []
#         for y_arr_y_idx in range(0, y_arr_xy[1]):
#             dW_row.append()
#         dW_row = -1*sum()
#     dW = -1/(y-p)
#
#     db = sum(p - y) / len(y)
#     b = b - (alpha * db)
#
#     dw = dot((p - y), x_new) / len(y)
#     w = w - (alpha * dw)
#
#     return b, w
#
#
# def backward_propagation():
#
#     return 0x0
#
#
#

def python_std_libs(data_dict, weight_size):
    data_input = list(data_dict.keys())
    data_output = list(data_dict.values())

    ret_weights = generate_weights(weight_size[0], weight_size[1], 1000)

    ret_bias = generate_bias(1, weight_size[1], 3)

    ### FORWARD PROPAGATION ###
    result = forward_propagation(data_input, data_output, ret_weights, ret_bias)
    print("Result=", result)
    ### BACKWARD PROPAGATION ###


if __name__ == '__main__':
    """
    Decimal to Binary NN Model
                      {        FORWARD PROPAGATION LAYER#1         }
        Input(4,1,1) -> {Hidden layer (1,8) -> Activation layer (1,8)}

        (1,8)*(4,1)
    """
    weight_dim = (1, 8)
    sample_data_dict = {
        # (4, 1, 1) : (4, 1, 8)
        ((0,),): [[0,0,0,0,0,0,0,0]],
        ((1,),): [[0,0,0,0,0,0,0,1]],
        ((2,),): [[0,0,0,0,0,0,1,0]],
        ((3,),): [[0,0,0,0,0,0,1,1]]
    }


    python_std_libs(sample_data_dict, weight_dim)
