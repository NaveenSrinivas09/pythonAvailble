{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOJAkxSc8NCTgySi6FKoFtb",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/NaveenSrinivas09/pythonAvailble/blob/main/similarityBWstring.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0j1fx-HInDHJ",
        "outputId": "1116b62b-7fc6-4045-990f-f48f7bf7f833"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0.75 ('python', 'pythonista')\n",
            "0.13333333333333333 ('python', 'developer')\n",
            "0.23529411764705882 ('python', 'development')\n",
            "0.10526315789473684 ('pythonista', 'developer')\n",
            "0.19047619047619047 ('pythonista', 'development')\n",
            "0.8 ('developer', 'development')\n"
          ]
        }
      ],
      "source": [
        "#similarity checking\n",
        "from itertools import combinations\n",
        "from collections import defaultdict\n",
        "from difflib import SequenceMatcher\n",
        "from functools import lru_cache\n",
        "\n",
        "tags = 'python pythonista developer development'.split()\n",
        "\n",
        "for i in combinations(tags, 2):\n",
        "    similarity = SequenceMatcher(None, *i).ratio()\n",
        "    print(similarity, i)\n",
        "\n",
        "\n"
      ]
    }
  ]
}