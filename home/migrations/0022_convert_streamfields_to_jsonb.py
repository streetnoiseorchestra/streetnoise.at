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
        ("home", "0021_alter_donationpage_donation_intro_and_more"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL(
                    sql="\n".join(
                        [
                            convert_columns_to_jsonb_sql(
                                "home_donationpage",
                                [
                                    "donation_intro",
                                    "donation_intro_de",
                                    "donation_intro_en",
                                ],
                            ),
                            convert_columns_to_jsonb_sql(
                                "home_festivalpage",
                                [
                                    "festival_program_timeline",
                                    "festival_program_timeline_de",
                                    "festival_program_timeline_en",
                                    "festival_program_content",
                                    "festival_program_content_de",
                                    "festival_program_content_en",
                                    "whoweare_gallery",
                                    "merch_items",
                                    "merch_items_de",
                                    "merch_items_en",
                                    "join_us_infos",
                                    "join_us_infos_de",
                                    "join_us_infos_en",
                                ],
                            ),
                            convert_columns_to_jsonb_sql(
                                "home_genericpage",
                                ["content", "content_de", "content_en"],
                            ),
                            convert_columns_to_jsonb_sql(
                                "home_homepage2",
                                [
                                    "whoweare_gallery",
                                    "merch_items",
                                    "merch_items_de",
                                    "merch_items_en",
                                    "join_us_infos",
                                    "join_us_infos_de",
                                    "join_us_infos_en",
                                ],
                            ),
                        ]
                    ),
                    reverse_sql="\n".join(
                        [
                            convert_columns_to_text_sql(
                                "home_donationpage",
                                [
                                    "donation_intro",
                                    "donation_intro_de",
                                    "donation_intro_en",
                                ],
                            ),
                            convert_columns_to_text_sql(
                                "home_festivalpage",
                                [
                                    "festival_program_timeline",
                                    "festival_program_timeline_de",
                                    "festival_program_timeline_en",
                                    "festival_program_content",
                                    "festival_program_content_de",
                                    "festival_program_content_en",
                                    "whoweare_gallery",
                                    "merch_items",
                                    "merch_items_de",
                                    "merch_items_en",
                                    "join_us_infos",
                                    "join_us_infos_de",
                                    "join_us_infos_en",
                                ],
                            ),
                            convert_columns_to_text_sql(
                                "home_genericpage",
                                ["content", "content_de", "content_en"],
                            ),
                            convert_columns_to_text_sql(
                                "home_homepage2",
                                [
                                    "whoweare_gallery",
                                    "merch_items",
                                    "merch_items_de",
                                    "merch_items_en",
                                    "join_us_infos",
                                    "join_us_infos_de",
                                    "join_us_infos_en",
                                ],
                            ),
                        ]
                    ),
                )
            ],
            state_operations=[],
        )
    ]
