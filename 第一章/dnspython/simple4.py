#!/usr/bin/env python
import dns.resolver

# domain = raw_input('Please input an domain: ')
domain="dearamaze.com"
cname = dns.resolver.query(domain, 'CNAME')
for i in cname.response.answer:
    for j in i.items:
        print j.to_text()

