from django.db import models
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class NumberBoxesBlock(blocks.StructBlock):
    boxes = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("value", blocks.CharBlock(required=True, max_length=40)),
                ("label", blocks.TextBlock(required=True, max_length=200)),
            ]
        )
    )

    class Meta:
        template = "festival2026/blocks/number_boxes_block.html"
        icon = "grip"
        label = "Number Boxes"


class LineupBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255)
    performers = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("name", blocks.CharBlock(required=True, max_length=255)),
                ("location", blocks.CharBlock(required=True, max_length=255)),
                ("website", blocks.URLBlock(required=False)),
                ("social", blocks.URLBlock(required=False)),
                ("logo", ImageChooserBlock(required=True)),
            ]
        )
    )

    class Meta:
        template = "festival2026/blocks/lineup_block.html"
        label = "Lineup"


class SponsorBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True, max_length=255)
    logo = ImageChooserBlock(required=False)
    url = blocks.URLBlock(required=False)


class FundersBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255)
    funders = blocks.ListBlock(SponsorBlock())

    class Meta:
        template = "festival2026/blocks/funders_block.html"
        label = "Funders"


class HeadingParagraphBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255)
    text = blocks.RichTextBlock(
        features=[
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "bold",
            "italic",
            "strikethrough",
            "ol",
            "ul",
            "hr",
            "link",
            "document-link",
            "image",
            "embed",
            "blockquote",
        ]
    )

    class Meta:
        template = "festival2026/blocks/heading_paragraph_block.html"
        label = "Heading + Paragraph"


class TimelineHeaderBlock(blocks.StructBlock):
    title = blocks.CharBlock()

    class Meta:
        template = "festival2026/blocks/timeline_header.html"


class TimelineItemBlock(blocks.StructBlock):
    icon = blocks.CharBlock()
    title = blocks.CharBlock(label="Time")
    detail = blocks.CharBlock(label="Name")
    small_detail = blocks.CharBlock(required=False, label="Extra Detail")

    class Meta:
        template = "festival2026/blocks/timeline_item.html"


class ProgramBlock2(blocks.StructBlock):
    heading = blocks.CharBlock(label="Program Section Heading")

    timeline = blocks.StreamBlock(
        [
            ("heading", TimelineHeaderBlock(label="Timeline Item Name")),
            ("item", TimelineItemBlock(label="Timeline Item Info")),
        ],
        label="Program Timeline Items",
    )
    descriptions = blocks.StreamBlock(
        [
            (
                "heading",
                blocks.CharBlock(classname="full title", label="Program Item Heading"),
            ),
            ("item", blocks.RichTextBlock(label="Program Item Description")),
        ],
        label="Program Descriptions",
    )

    class Meta:
        template = "festival2026/blocks/program_block.html"


class CrowdfundingRewardItemBlock(blocks.StructBlock):
    """A block for displaying a single reward for the crowdfunding campaign.
    With the fields:
    * title: The title of the reward
    * description: A description of the reward
    * image: An image for the reward
    * price: The price of the reward
    * payment_link: the Stripe url to the reward
    """

    title = blocks.CharBlock(required=True, max_length=255)
    description = blocks.TextBlock(required=True, max_length=255)
    image = ImageChooserBlock(required=False)
    price = blocks.CharBlock(required=True, max_length=255)
    payment_link = blocks.URLBlock(required=True)

    class Meta:
        template = "festival2026/blocks/crowdfunding_reward_item_block.html"
        label = "Crowdfunding Reward Item"


class CrowdfundingRewardsBlock(blocks.StructBlock):
    """A block for displaying the rewards for the crowdfunding campaign.
    With the fields:
    * heading: The heading for the block
    * rewards: A block.ListBLock list of CrowdfundingRewardItemBlock
    """

    heading = blocks.CharBlock(required=True, max_length=255)
    description2 = blocks.RichTextBlock(
        features=[
            "bold",
            "italic",
            "strikethrough",
            "ol",
            "ul",
            "hr",
            "link",
            "document-link",
            "image",
            "blockquote",
        ]
    )
    rewards = blocks.ListBlock(CrowdfundingRewardItemBlock())

    class Meta:
        template = "festival2026/blocks/crowdfunding_rewards_block.html"
        label = "Crowdfunding Rewards"
