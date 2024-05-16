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


def neuron_compute_np(x_input, weights, bias):
    Act = ActivationClass()

    print("weights=", weights.shape)
    print("x_input=", x_input.shape)

    Z = np.dot(x_input, weights) + bias
    print("Z=", Z.shape)

    # TODO: Add assertion to get correct size after matrix multiplication

    A = Act.sigmoid(Z)
    print("A=", A)
    print("A=", A.shape)

    # TODO: Add assertion to get correct size after matrix computation

    return A


def cost_function_np(compute, sample):
    func_a = np.multiply(sample, np.log(compute))
    func_b = np.multiply((1 - sample), np.log(1 - compute))

    log_cost = func_a + func_b
    print("LOGCOST = ", log_cost)
    print("LOGCOST = ", log_cost.shape)

    cost = (-1 / compute.shape[0]) * np.sum(log_cost)

    return cost


def forward_propagation_np(data_input, data_output, weights, bias):
    A = neuron_compute_np(data_input, weights, bias)
    Y = cost_function_np(A, data_output)

    return Y

# ######################################### BACK PROPAGATION #########################################


def numpy_libs(data_dict, weight_size):
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

    print("DATA IN=", data_input)
    print("DATA IN=", data_input.shape)
    print("DATA OUT=", data_output)
    print("DATA OUT=", data_output.shape)

    weight_arr = generate_weights_np(weight_size)
    bias_arr = generate_bias_np(weight_size)

    Y = forward_propagation_np(data_input, data_output, weight_arr, bias_arr)
    print("COST=", Y)


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
