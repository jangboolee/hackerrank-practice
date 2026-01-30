def whatFlavors(cost: list[int], money: int) -> None:
    idxs = {}
    for i, price in enumerate(cost):
        # Calculate required pair price
        req_price = money - price
        # Check if required pair price has been seen
        req_price_idx = idxs.get(req_price)
        if req_price_idx:
            print(req_price_idx, i + 1)
        # If the required pair price has not been seen
        else:
            # Save the current price for future use with 1-index
            idxs[price] = i + 1

def test(fn) -> None:
  case_0_cost = [2, 1, 3, 5, 6]
  case_0_money = 5


if __name__ == "__main__:
  test(whatFlavors)
