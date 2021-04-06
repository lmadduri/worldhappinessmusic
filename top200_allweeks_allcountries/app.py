from fycharts.SpotifyCharts import SpotifyCharts
import time

# regions = ["us", "gb", "ad", "ar", "at", "au", "be", "bg",
#                "bo", "br", "ca", "ch", "cl", "co", "cr", "cy", "cz", "de",
#                "dk", "do", "ec", "ee", "es", "fi", "fr", "gr", "gt", "hk",
#                "hn", "hu", "id", "ie", "is", "it", "jp", "lt", "lu", "lv",
#                "mc", "mt", "mx", "my", "ni", "nl", "no", "nz", "pa", "pe",
#                "ph", "pl", "pt", "py", "se", "sg", "sk", "sv", "tr", "tw", "uy"]
#
api = SpotifyCharts()
# for region in regions:
#     filename = "top_200_weekly_"+region+"_2021.csv"
#     api.top200Weekly(output_file=filename, start="2016-01-13", end="2016-12-30", region=region)
#     time.sleep(120)


filename = "top_200_weekly_jp_2017.csv"
api.top200Weekly(output_file=filename, start="2017-09-01", end="2017-12-30", region="jp")