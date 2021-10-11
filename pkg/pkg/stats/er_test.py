from scipy.stats import ttest_ind


def erdos_reyni_test(A1, A2, method='t'):
    # TODO adjust to properly handle the loops
    if method == 't':
        stat, pvalue = ttest_ind(
            A1.ravel(), A2.ravel(), equal_var=False, alternative="two-sided"
        )
    elif method == 'fisher':
        # TODO should we replace with Fisher's exact test?
        raise NotImplementedError()
    return stat, pvalue, {}
