def get_country_codes(prices):
  new_list = [char for char in prices if char.isalpha() or char == " " or char == ","]
  new_string = ""
  for item in new_list:
    new_string+=item
  return new_string

print(get_country_codes("NZ$300, KR$1200, DK$5"))
print(get_country_codes("US$40, AU$89, JP$200"))
print(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"))
print(get_country_codes("CA$40"))