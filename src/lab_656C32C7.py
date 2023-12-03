import pandas as pd

data = {
  "LOCATION": ["CENTRAL", "MA ON SHAN", "TSIM SHA TSUI"],
  "TEMPERATURE": [22, 21, 20]
}

def main():
    df = pd.DataFrame(data)
    print(df)

if __name__ == '__main__':
    main()