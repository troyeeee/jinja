# -*- coding: utf-8 -*-
# byoryn filter functions
# Built-in template filters used with the ``|`` operator.
import math

from .exceptions import FilterArgumentError


def do_double_col(s, attribute=None):
    """
    resoure data from panel (record format: [ [ [], [] ], [ [], [] ],,,....])
    reformating data into[[[],[],[],[]][[],[],[],[]],...]

    .. sourcecode:: jinja

        {% for item in dataframe|double_col %}
            default set Disease & Gene as the double columns

        {% for item in dataframe|double_col(key="Disease, Gene") %}
            display item.Disease item.Gene in double columns
    """

    check_attr_valid(s, attribute)
    dis_gene_tmp = []
    dis_gene = []
    first = attribute[0]
    second = attribute[1]
    for idx, record in s.iterrows():
        dis_gene_tmp.append([record[first], record[second].strip()])
    j = 0
    for i in range(0, math.ceil(len(dis_gene_tmp)/2)):
        if len(dis_gene_tmp) - i*2 == 1:
            dis_gene.append([dis_gene_tmp[j][0], dis_gene_tmp[j][1], ' ',
                            '', ''])
        else:
            dis_gene.append([dis_gene_tmp[j][0], dis_gene_tmp[j][1], ' ',
                            dis_gene_tmp[j+1][0], dis_gene_tmp[j+1][1]])
            j += 2
    return dis_gene


def do_pie(s):
    return s


def do_line(s):
    return s


def check_attr_valid(df, attr):
    col_name = df.columns.values
    for i in attr:
        if i not in col_name:
            raise FilterArgumentError("attribute "+i+" not found" )


''' "filterName": process function '''
BYORYN_FILTERS = {
    "double_col":  do_double_col
}