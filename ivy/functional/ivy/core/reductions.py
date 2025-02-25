"""
Collection of reduction Ivy functions
"""

# local
import ivy
from ivy.framework_handler import current_framework as _cur_framework


def reduce_sum(x, axis=None, keepdims=False):
    """
    Computes sum of array elements along a given axis.

    :param x: Elements to sum.
    :type x: array
    :param axis: Axis or axes along which a sum is performed. The default, axis=None, will sum all of the elements of
                    the input array. If axis is negative it counts from the last to the first axis.
                    If axis is a tuple of ints, a sum is performed on all of the axes specified in the tuple instead of
                    a single axis or all the axes as before.
    :type axis: int or sequence of ints
    :param keepdims: If this is set to True, the axes which are reduced are left in the result as dimensions with size
                        one. With this option, the result will broadcast correctly against the input array.
    :type keepdims: bool, optional
    :return: The array with sums computed.
    """
    return _cur_framework(x).reduce_sum(x, axis, keepdims)


def reduce_prod(x, axis=None, keepdims=False):
    """
    Multiplies array elements along a given axis.

    :param x: Elements to multiply.
    :type x: array
    :param axis: Axis or axes along which a multiplication is performed. The default, axis=None, will multiply all of
                 the elements of the input array. If axis is negative it counts from the last to the first axis.
                 If axis is a tuple of ints, a multiplication is performed on all of the axes specified in the tuple
                 instead of a single axis or all the axes as before.
    :type axis: int or sequence of ints
    :param keepdims: If this is set to True, the axes which are reduced are left in the result as dimensions with size
                        one. With this option, the result will broadcast correctly against the input array.
    :type keepdims: bool, optional
    :return: The array with multiplications computed.
    """
    return _cur_framework(x).reduce_prod(x, axis, keepdims)


def reduce_mean(x, axis=None, keepdims=False):
    """
    Computes the arithmetic mean along a given axis.
    Returns the average of the array elements. The average is taken over the flattened array by default, otherwise over
    the specified axis.

    :param x: Array containing numbers whose mean is desired.
    :type x: array
    :param axis: Axis or axes along which the means are computed. The default is to compute the mean of the flattened
                    array. If this is a tuple of ints, a mean is performed over multiple axes, instead of a single axis
                    or all the axes as before.
    :type axis: int or sequence of ints
    :param keepdims: If this is set to True, the axes which are reduced are left in the result as dimensions with size
                        one. With this option, the result will broadcast correctly against the input array.
    :type keepdims: bool, optional
    :return: The array with means computed.
    """
    return _cur_framework(x).reduce_mean(x, axis, keepdims)


def reduce_var(x, axis=None, keepdims=False):
    """
    Computes the arithmetic variance along a given axis. The variance is taken over the flattened array by default,
    otherwise over the specified axis.

    :param x: Array containing numbers whose variance is desired.
    :type x: array
    :param axis: Axis or axes along which the means are computed. The default is to compute the mean of the flattened
                    array. If this is a tuple of ints, a mean is performed over multiple axes, instead of a single axis
                    or all the axes as before.
    :type axis: int or sequence of ints
    :param keepdims: If this is set to True, the axes which are reduced are left in the result as dimensions with size
                        one. With this option, the result will broadcast correctly against the input array.
    :type keepdims: bool, optional
    :return: The array with variances computed.
    """
    return _cur_framework(x).reduce_var(x, axis, keepdims)


def reduce_std(x, axis=None, keepdims=False):
    """
    Computes the arithmetic standard deviation along a given axis. The standard deviation is taken over
    the flattened array by default, otherwise over the specified axis.

    :param x: Array containing numbers whose standard deviation is desired.
    :type x: array
    :param axis: Axis or axes along which the means are computed. The default is to compute the mean of the flattened
                    array. If this is a tuple of ints, a mean is performed over multiple axes, instead of a single axis
                    or all the axes as before.
    :type axis: int or sequence of ints
    :param keepdims: If this is set to True, the axes which are reduced are left in the result as dimensions with size
                        one. With this option, the result will broadcast correctly against the input array.
    :type keepdims: bool, optional
    :return: The array with standard deviations computed.
    """
    return ivy.array(ivy.reduce_var(x, axis, keepdims) ** 0.5)


def reduce_min(x, axis=None, keepdims=False):
    """
    Computes the minimum value along the specified axis. The minimum is taken over the flattened array by default,
    otherwise over the specified axis.

    :param x: Array containing numbers whose min is desired.
    :type x: array
    :param axis: Axis or axes along which the mins are computed. The default is to compute the min of the flattened
                    array. If this is a tuple of ints, a min is performed over multiple axes, instead of a single axis
                    or all the axes as before.
    :type axis: int or sequence of ints
    :param keepdims: If this is set to True, the axes which are reduced are left in the result as dimensions with size
                        one. With this option, the result will broadcast correctly against the input array.
    :type keepdims: bool, optional
    :return: The array with mins computed.
    """
    return _cur_framework(x).reduce_min(x, axis, keepdims)


def max(x, axis=None, keepdims=False):
    """
    Computes the maximum value along the specified axis. The maximum is taken over the flattened array by default,
    otherwise over the specified axis.

    :param x: Array containing numbers whose max is desired.
    :type x: array
    :param axis: Axis or axes along which the maxes are computed. The default is to compute the max of the flattened
                    array. If this is a tuple of ints, a max is performed over multiple axes, instead of a single axis
                    or all the axes as before.
    :type axis: int or sequence of ints
    :param keepdims: If this is set to True, the axes which are reduced are left in the result as dimensions with size
                        one. With this option, the result will broadcast correctly against the input array.
    :type keepdims: bool, optional
    :return: The array with maxes computed.
    """
    return _cur_framework(x).max(x, axis, keepdims)


def einsum(equation, *operands):
    """
    Sums the product of the elements of the input operands along dimensions specified using a notation based on the
    Einstein summation convention.

    :param equation: A str describing the contraction, in the same format as numpy.einsum.
    :type equation: str
    :param operands: the inputs to contract (each one an ivy.Array), whose shapes should be consistent with equation.
    :type operands: seq of arrays
    :return: The array with sums computed.
    """
    return _cur_framework(operands[0]).einsum(equation, *operands)