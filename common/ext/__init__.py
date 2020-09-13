""" Convert yaml to python.

Usage:
    # convert to JSON format testcase


"""

from argparse import ArgumentParser


from common.ext.make import read_py_file, gen_py_template


def init_yaml_2py_page_parser(parser: ArgumentParser):
    """ yaml converter: parse command line options and run commands.
    """

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-Y", "--yaml_source_file", nargs="?", dest="yaml_source_file", help="Specify YAML source file")

    return parser


def main_yaml_2py_page(args):

    if args.yaml_source_file:
        res = read_py_file(
            rf'{args.yaml_source_file}')
        gen_py_template(*res)


