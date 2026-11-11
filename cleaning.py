import pandas as pd
df = pd.read_csv("hotel_bookings.csv")
print(df.head())
print(df.shape)
print(df.isnull().sum())
print(df.isnull().mean() * 100)
print(df.duplicated().sum())
print(df[df.duplicated()].head)
df=df.drop_duplicates()
print(df.shape)
print(df.duplicated().sum())
print(df["company"].isnull().sum())
print(df.isnull().mean() * 100)
print(df["children"].value_counts(dropna=False))
print(df["children"].median())
df["children"] = df["children"].fillna(0)
df["country"] = df["country"].fillna("Unknown")
print(df["country"].value_counts(dropna=False).head(25))
print(df["agent"].value_counts(dropna=False))
df["agent"]=df["agent"].fillna("Unknown")
df["agent"].value_counts().head(25)
print(df["company"].value_counts(dropna=False).head(20))
df = df.drop(columns=["company"])
df.info()
df["reservation_status_date"] = pd.to_datetime(df["reservation_status_date"])
print(df["reservation_status_date"].dtype)

print(df[df["adults"] >= 20][["adults", "children", "babies", "stays_in_weekend_nights", "stays_in_week_nights"]])
print(df[df["adults"] >= 20][["adults", "is_canceled", "market_segment", "customer_type", "reservation_status"]])

print(df[df["adults"] == 0][["adults", "children", "babies", "stays_in_weekend_nights", "stays_in_week_nights", "is_canceled"]])
df.drop(df[df["adults"] == 0].index, inplace=True)

print(df["reservation_status_date"].value_counts().head(10))

df["children"] = df["children"].astype(int)

print(df.shape)
print(df.isnull().sum().sum())
print(df.duplicated().sum())

print(df[df.duplicated(keep=False)])
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())

df.to_csv("hotel_cleaned.csv", index=False)

print(df[df["adr"] < 0][["adr", "is_canceled", "reservation_status", "adults", "children", "stays_in_weekend_nights", "stays_in_week_nights"]])

print(df[df["adr"] == 0][["adr", "is_canceled", "reservation_status", "adults", "children", "babies", "stays_in_weekend_nights", "stays_in_week_nights"]])

# حساب متوسط ADR بدون القيم الصفرية والسالبة
adr_average = df.loc[df["adr"] > 0, "adr"].mean()

print("ADR Average:", adr_average)

# استبدال القيم الصفرية والسالبة بالمتوسط
df.loc[df["adr"] <= 0, "adr"] = adr_average

# التأكد من عدم وجود قيم صفرية أو سالبة
print("Zero ADR:", (df["adr"] == 0).sum())
print("Negative ADR:", (df["adr"] < 0).sum())

# حفظ الملف بعد التنظيف
df.to_csv("hotel_cleaned.csv", index=False)