# Generated manually during the Wagtail 7 upgrade.

from django.db import migrations


def convert_columns_to_jsonb_sql(table_name, columns):
    statements = []
    for column in columns:
        quoted_table = f'"{table_name}"'
        quoted_column = f'"{column}"'
        statements.append(
            f"""
ALTER TABLE {quoted_table}
    ALTER COLUMN {quoted_column} TYPE jsonb
    USING CASE
        WHEN {quoted_column} IS NULL THEN NULL
        WHEN btrim({quoted_column}::text) = '' THEN '[]'::jsonb
        ELSE {quoted_column}::jsonb
    END;
""".strip()
        )
    return "\n".join(statements)


def convert_columns_to_text_sql(table_name, columns):
    statements = []
    for column in columns:
        quoted_table = f'"{table_name}"'
        quoted_column = f'"{column}"'
        statements.append(
            f"""
ALTER TABLE {quoted_table}
    ALTER COLUMN {quoted_column} TYPE text
    USING CASE
        WHEN {quoted_column} IS NULL THEN NULL
        ELSE {quoted_column}::text
    END;
""".strip()
        )
    return "\n".join(statements)


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0018_alter_blogpage_body_alter_blogpage_body_de_and_more"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL(
                    sql=convert_columns_to_jsonb_sql(
                        "blog_blogpage",
                        ["body", "body_de", "body_en"],
                    ),
                    reverse_sql=convert_columns_to_text_sql(
                        "blog_blogpage",
                        ["body", "body_de", "body_en"],
                    ),
                )
            ],
            state_operations=[],
        )
    ]
