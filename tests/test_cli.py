import pytest
from twittercli import cli


@pytest.fixture()
def parser():
    parser = cli.create_parser()
    return parser


def test_parser_no_args(parser):
    assert parser.parse_args([])


def test_parser_with_one_option_no_arg(parser):
    with pytest.raises(SystemExit):
        parser.parse_args(['-t'])
        parser.parse_args(['-u'])
        parser.parse_args(['-s'])


def test_parser_with_invalid_argument(parser):
    with pytest.raises(SystemExit):
        parser.parse_args(['-w'])


def test_parser_with_one_option_one_arg(parser):
    assert parser.parse_args(['-u test'])
    assert parser.parse_args(['-s test'])
    assert parser.parse_args(['-t test'])
