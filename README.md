# zenn-article-aggregator
A tool to retrieve the titles, links, and authors of articles posted to Zenn's Publication and aggregate them into Notion's DB.

[日本語ドキュメント](README_JP.md)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Demo](#demo)
- [Setup](#setup)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Demo

The data acquired at [MidraLab HP](https://midra-lab.notion.site/7ab2d6ad6b5e4c6487220ac360e6d8ec?v=340f109e5ced4ae99afad0f0ea4c8c62) is reflected in the following image.

![](Docs/Demo.png)

# Setup
1. obtain the NotionAPI token and the Id of the Notion DB you wish to reflect
2. set the NotionAPI token to the environment variable of GitHub Actions
Fork Repository and change `publication_url` in `main.py` to your Publication's URL