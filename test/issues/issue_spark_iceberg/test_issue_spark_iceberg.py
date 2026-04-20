from morph_kgc.constants import HIVE, SPARK, SPARKSQL
from morph_kgc.data_source.relational_db import _replace_query_enclosing_characters


def test_keep_backticks_for_spark():
    query = "SELECT `id`, `name` FROM `catalog`.`db`.`iceberg_table`"
    assert _replace_query_enclosing_characters(query, SPARK) == query


def test_keep_backticks_for_sparksql():
    query = "SELECT `id`, `name` FROM `catalog`.`db`.`iceberg_table`"
    assert _replace_query_enclosing_characters(query, SPARKSQL) == query


def test_keep_backticks_for_hive():
    query = "SELECT `id`, `name` FROM `catalog`.`db`.`iceberg_table`"
    assert _replace_query_enclosing_characters(query, HIVE) == query
