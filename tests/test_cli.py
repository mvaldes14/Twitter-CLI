import pytest
from twittercli import cli


@pytest.fixture()
def parser():
    parser = cli.create_parser()
    return parser


def test_parser_no_args(parser):
    assert parser.parse_args([])


@pytest.mark.parametrize('argument',[
    '-t',
    '-u',
    '-s'
])
def test_parser_with_one_option_no_arg(parser, argument):
    with pytest.raises(SystemExit):
        parser.parse_args([argument])
        


def test_parser_with_invalid_argument(parser):
    with pytest.raises(SystemExit):
        parser.parse_args(['-w'])


@pytest.mark.parametrize('argument',[
    '-t test',
    '-u test',
    '-s test'
])
def test_parser_with_one_option_one_arg(parser, argument):
    assert parser.parse_args([argument])