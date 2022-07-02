import twint
#configuration
config = twint.Config()
search_value = ["NFT", "nftcollector", "nftart", "nfts", "nftartist", "nftcommunity", "nftsale", "nftshowcase", "nftshop", "nftcreators", "nftblog", "nftnews", "nftstyle", "nftmagazine", "nftcollectibles"]
for x in search_value:
	config.Search = x
	config.Lang = "en"
	config.Limit = 10000
	#config.Since = "2022–04–01"
	#config.Until = "2022–06–30"
	config.Store_txt = True
	config.Output = "file.txt"
	#running search
	twint.run.Search(config)
search_username = ["nftmarket", "nftshowroom", "nftnews", "nfttrader", "nftcollector", "nftinvestor", "nftartist", "nftcreators", "NFTNews", "NFTMarket", "NFTInvesting", "NFTTrading", "NFTsales", "NFTs_", "NFT_Marketplace", "NFTSales", "NFT_Trading", "NFT_Investing"]
for u in search_username:
        config.Search = "from:@{}".format(u)
        config.Lang = "en"
        config.Limit = 10000
        #config.Since = "2022–04–01"
        #config.Until = "2022–06–30"
        config.Store_txt = True
        config.Output = "file.txt"
        #running search
        twint.run.Search(config)
