import pandas as pd

from src.infra.database.repository import CryptoRepository


class GetCryptoDashboardData:

    def __init__(self):
        self.repository = CryptoRepository()


    def execute(self):

        data = self.repository.get_all()


        columns = [
            "id",
            "name",
            "symbol",
            "currency",
            "current_price",
            "market_cap",
            "total_volume",
            "price_change_percentage_24h",
            "last_updated"
        ]


        df = pd.DataFrame(
            data,
            columns=columns
        )


        latest_df = (
            df
            .sort_values(by="last_updated")
            .drop_duplicates(
                subset=["symbol"],
                keep="last"
            )
        )


        return df, latest_df