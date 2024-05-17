import numpy as np

from Activation_Class import ActivationClass


def generate_weights_np(dimension, b_as_zeroes=False):
    if b_as_zeroes:
        w = np.zeros(dimension)
    else:
        w = np.random.randn(dimension[0], dimension[1])

    # print("W=", w.shape)

    assert len(w) == dimension[0], "Weight dimension X did not match to " + str(dimension[0])
    assert len(w[0]) == dimension[1], "Weight dimension Y did not match to " + str(dimension[1])

    return w


def generate_bias_np(dimension, b_as_zeroes=False):
    if b_as_zeroes:
        b = np.zeros((1, dimension[1]))
    else:
        b = np.random.randn(1, dimension[1])

    # print("B=", b.shape)

    assert len(b) == dimension[0], "Weight dimension X did not match to " + str(dimension[0])
    assert len(b[0]) == dimension[1], "Weight dimension Y did not match to " + str(dimension[1])

    return b


def neuron_compute_np(x_input, params):
    Act = ActivationClass()

    weights = params["weights"]
    bias = params["bias"]

    print("weights=", weights.shape)
    print("x_input=", x_input.shape)

    Z = np.dot(x_input, weights) + bias
    print("Z=", Z.shape)

    # TODO: Add assertion to get correct size after matrix multiplication

    A = Act.sigmoid(Z)
    # print("A=", A)
    print("A=", A.shape)

    # TODO: Add assertion to get correct size after matrix computation

    params['A'] = A
    params['Z'] = Z

    return params


def cost_function_np(params, sample, cost_dict):
    compute = params['A']

    func_a = np.multiply(sample, np.log(compute))
    func_b = np.multiply((1 - sample), np.log(1 - compute))

    log_cost = func_a + func_b
    # print("LOGCOST = ", log_cost)
    print("LOGCOST = ", log_cost.shape)

    cost_dict['cost'] = (-1 / compute.shape[0]) * np.sum(log_cost)

    return cost_dict


def forward_propagation_np(data_input, data_output, params):
    cost_dict = {}

    params = neuron_compute_np(data_input, params)
    cost_dict = cost_function_np(params, data_output, cost_dict)

    return params, cost_dict


# ######################################### BACK PROPAGATION #########################################
def backward_propagation_np(data_input, data_output, params):
    computed, weights, bias = params['A'], params['weights'], params['bias']

    print(data_input.shape)
    print(data_output.shape)
    print(computed.shape)

    act_y = computed - data_output

    print("A-Y = ", act_y)

    dW = np.multiply(1/data_input.shape[0], np.multiply(data_input, (computed - data_output)))

    dB = np.multiply(1/data_input.shape[0], (computed-data_output))

    print("dW=", dW)
    print("dB=", dB)

    print("dW=", dW.shape)
    print("dB=", dB.shape)

    return dW, dB


def input_processing(data_sample: dict):
    """
    dict -> input(1,1,N) and output(1,8,N)

    :param data_sample:
    :type data_sample:
    :return:
    :rtype:
    """

    data_input = np.array(list(data_sample.keys()))
    data_input = np.reshape(data_input, (4,1,1))

    data_output = np.array(list(data_sample.values()))
    data_output = np.reshape(data_output, (4,1,8))
    #
    # print(data_input.shape)
    # print(data_input)
    # print(data_output.shape)
    # print(data_output)

    return False, False


def numpy_libs(data_dict, weight_size):

    nn_parameters = {}

    data_input, data_output = input_processing(data_dict)

    data_input = list(data_dict.keys())
    data_output = list(data_dict.values())

    data_input = np.array(data_input)
    data_output = np.array(data_output)

    # For manipulating Array dimensions
    # data_input = np.stack(data_input)
    # data_output = np.stack(data_output)
    #
    # data_input = np.prod(data_input, axis=1)
    # data_output = np.prod(data_output, axis=1)

    # print("DATA IN=", data_input)
    # print("DATA IN=", data_input.shape)
    # print("DATA OUT=", data_output)
    # print("DATA OUT=", data_output.shape)

    # weight_arr = generate_weights_np(weight_size)
    # bias_arr = generate_bias_np(weight_size)
    # cost, A = forward_propagation_np(data_input, data_output, weight_arr, bias_arr)

    nn_parameters['weights'] = generate_weights_np(weight_size)
    nn_parameters['bias'] = generate_bias_np(weight_size)
    nn_parameters, cost_dict = forward_propagation_np(data_input, data_output, nn_parameters)

    print("COST=", cost_dict)

    ret = backward_propagation_np(data_input, data_output, nn_parameters)
    # print("RET=", ret)


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

    numpy_libs(sample_data_dict, weight_dim)