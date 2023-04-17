import logging

from pybit.unified_trading import HTTP
from bybit_early_reaction_job.bybit_early_reaction_job_helper import BybitEarlyReactionJobHelper as Helper


class BybitEarlyReactionJob:

    def __init__(self, config: dict) -> None:
        self.config = config
        self.pybit_client = HTTP(testnet=True,
                                 api_key=self.config["bybitApi"]["apiKey"],
                                 api_secret=self.config["bybitApi"]["secretKey"])

    def run(self) -> None:
        logging.info("Start job")

        logging.info("Get available tickers")
        tickers = Helper.get_available_tickers()
        logging.debug("Available tickers: {}".format(tickers))

        logging.info("Process tickers")
        for ticker in tickers:
            last_close_pnl = Helper.get_last_close_pnl(ticker)

            if last_close_pnl is None:
                continue

            if last_close_pnl["amount"] > self.pnl_limit and last_close_pnl["date"] < "now - minutes_limit":
                continue

            logging.info("Early reaction on ticker: {}".format(ticker))

            logging.info("Close positions")
            Helper.close_positions(ticker)

            logging.info("Close open orders")
            Helper.close_open_orders(ticker)

        logging.info("Finished job")
