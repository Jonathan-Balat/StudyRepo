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

    # print("weights=", weights.shape)
    # print("x_input=", x_input.shape)

    Z = np.dot(x_input, weights) + bias
    # print("Z=", Z.shape)

    # TODO: Add assertion to get correct size after matrix multiplication

    A = Act.sigmoid(Z)
    # print("A=", A)
    # print("A=", A.shape)

    # TODO: Add assertion to get correct size after matrix computation

    params['A'] = A
    params['Z'] = Z

    return params


def neuron_test_np(x_input, params):
    Act = ActivationClass()

    weights = params["weights"]
    bias = params["bias"]

    # print("weights=", weights.shape)
    # print("x_input=", x_input.shape)

    Z = np.dot(x_input, weights) + bias
    # print("Z=", Z.shape)

    # TODO: Add assertion to get correct size after matrix multiplication

    A = Act.sigmoid(Z)
    A_min = np.min(A, axis=1)
    A_max = np.max(A, axis=1)

    print("NORMALIZED", A/(A_max - A_min))
    # print("A=", A)
    # print("A=", A.shape)

    return A


def cost_function_np(params, sample):
    compute = params['A']

    func_a = np.multiply(sample, np.log(compute))
    func_b = np.multiply((1 - sample), np.log(1 - compute))

    log_cost = func_a + func_b
    # print("LOGCOST = ", log_cost)
    # print("LOGCOST = ", log_cost.shape)

    cost = (-1 / compute.shape[0]) * np.sum(log_cost)

    return cost


# ######################################### BACK PROPAGATION #########################################
def backward_propagation_np(data_input, data_output, params):
    computed, weights, bias, alpha = params['A'], params['weights'], params['bias'], params['alpha']

    # print("X=", data_input.shape)
    # print("Y=", data_output.shape)
    # print("A=", computed.shape)

    act_y = computed - data_output

    dB = np.multiply(1/data_input.shape[0], (computed-data_output))
    # print("dB=", dB.shape)
    # print("dB=", dB)

    dW = np.multiply(1/data_input.shape[0], np.multiply(data_input, (computed - data_output)))
    # print("dW=", dW.shape)
    # print("dW=", dW)

    weights = weights - np.multiply(alpha, dW)
    bias = bias - np.multiply(alpha, dB)

    # print("weights =", weights)
    # print("bias =", bias)

    params['dW'] = dW
    params['dB'] = dB
    params['weights'] = weights
    params['bias'] = bias

    return params


def input_processing(data_sample: dict):
    """
    dict -> input(1,1,N) and output(1,8,N)

    :param data_sample:
    :type data_sample:
    :return:
    :rtype:
    """

    data_input = np.array(list(data_sample.keys()))
    data_input = np.reshape(data_input, (len(data_input),1,1))

    data_output = np.array(list(data_sample.values()))
    data_output = np.reshape(data_output, (len(data_input),1,8))

    # print(data_input.shape)
    # print(data_input)
    # print(data_output.shape)
    # print(data_output)

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

    return data_input, data_output


def numpy_libs(data_dict, weight_size):

    # Setup
    nn_parameters = {'alpha': 0.05}
    cost_dict = {}

    data_input, data_output = input_processing(data_dict)

    nn_parameters['weights'] = generate_weights_np(weight_size)
    nn_parameters['bias'] = generate_bias_np(weight_size)

    # Train
    for iteration in range(0, 10000):
        for data_idx in range(0, len(data_input)):
            x_data = data_input[0]
            y_data = data_output[0]
            # Compute and Optimize

            nn_parameters = neuron_compute_np(x_data, nn_parameters)
            cost_dict[data_idx] = cost_function_np(nn_parameters, y_data)

            nn_parameters = backward_propagation_np(x_data, y_data, nn_parameters)

        if iteration % 1000 == 0:
            # print("COST=")
            # for idx in range(0, len(cost_dict.keys())):
                # print("\t%d)"%idx, 100*cost_dict.get(idx), "%")
            print("\tCOSTave=", 100*sum(list(cost_dict.values()))/len(cost_dict.values()), "%")

    # Test Existing data
    for number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("\n", number, ")")
        binary_result = neuron_test_np(number, nn_parameters)
        print("-->", binary_result)


def __data_bin_generate(max_value=255):
    data = {}
    for number in range(0, max_value+1):
        tmp_inner = [(1 & (number >> idx)) for idx in range(0, 8)]
        tmp_inner.reverse()
        data[((number,),)] = [tmp_inner]
    return data

if __name__ == '__main__':
    """
    Decimal to Binary NN Model
                      {        FORWARD PROPAGATION LAYER#1         }
        Input(4,1,1) -> {Hidden layer (1,8) -> Activation layer (1,8)}

        (1,8)*(4,1)
    """
    weight_dim = (1, 8)
    # sample_data_dict = {
    #     # (4, 1, 1) : (4, 1, 8)
    #     ((1,),): [[0,0,0,0,0,0,0,1]],
    #     ((2,),): [[0,0,0,0,0,0,1,0]],
    #     ((3,),): [[0,0,0,0,0,0,1,1]],
    #     ((4,),): [[0,0,0,0,0,1,0,0]],
    #     ((5,),): [[0,0,0,0,0,1,0,1]],
    #     ((6,),): [[0,0,0,0,0,1,1,0]],
    #     ((7,),): [[0,0,0,0,0,1,1,1]],
    #     ((8,),): [[0,0,0,0,1,0,0,0]],
    # }
    sample_data_dict = __data_bin_generate()

    numpy_libs(sample_data_dict, weight_dim)