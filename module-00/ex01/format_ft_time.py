import datetime as dt

now = dt.datetime.now()
epoch = dt.datetime(1970, 1, 1, 0, 0, 0, 0)

diff_in_sec = (now - epoch).total_seconds()
diff_in_sec_formatted = f"{diff_in_sec:,.4f}"
diff_in_sec_scientific = f"{diff_in_sec:.2e}"

print(f"Seconds since January 1, 1970: {diff_in_sec_formatted} or {diff_in_sec_scientific} in scientific notation")
print(now.strftime("%b %d %Y"))