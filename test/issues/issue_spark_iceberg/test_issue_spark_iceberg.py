import pytest

from morph_kgc.constants import HIVE, SPARK, SPARKSQL
from morph_kgc.data_source.relational_db import _replace_query_enclosing_characters


@pytest.mark.parametrize('dialect', [SPARK, SPARKSQL, HIVE])
def test_keep_backticks_for_spark_family_dialects(dialect):
    query = "SELECT `id`, `name` FROM `catalog`.`db`.`iceberg_table`"
    assert _replace_query_enclosing_characters(query, dialect) == query
