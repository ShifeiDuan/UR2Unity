import numpy as np
import matplotlib.pyplot as plt

def calculate_monthly_cost(price_per_kwh, daily_charge, paid_usage, free_usage, days_per_month=30):
    """ 计算每月总电费 """
    daily_cost = daily_charge + (paid_usage * price_per_kwh)  # 只计算收费部分的用电量
    return daily_cost * days_per_month

def plot_cost_curves(companies, max_paid_usage=50, days_per_month=30):
    """ 绘制电费随收费用电量变化的曲线 """
    paid_usages = np.arange(0, max_paid_usage + 1, 1)  # 0 到 max_paid_usage，每隔 1 递增
    plt.figure(figsize=(10, 6))

    for company, data in companies.items():
        monthly_costs = [
            calculate_monthly_cost(data["price_per_kwh"], data["daily_charge"], pu, data["free_usage"], days_per_month)
            for pu in paid_usages
        ]
        plt.plot(paid_usages, monthly_costs, label=company, linewidth=2)

    plt.xlabel("usage (kwh)", fontsize=12)
    plt.ylabel("fee", fontsize=12)
    plt.title("comparision", fontsize=14)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

def main():
    # 每家公司电费信息
    companies = {
        "contact": {"price_per_kwh": 0.332, "daily_charge": 1.2, "free_usage": 10},
        "meridian": {"price_per_kwh": 0.3066, "daily_charge": 1.38, "free_usage": 10},
        # "C": {"price_per_kwh": 0.4, "daily_charge": 1.5, "free_usage": 3},
    }

    plot_cost_curves(companies, max_paid_usage=10, days_per_month=30)  # 最高收费用电量设为 50 度

if __name__ == "__main__":
    main()
