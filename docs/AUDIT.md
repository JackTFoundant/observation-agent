# Audit sample

25 citations chosen at random (seed 7) from the published report, with the
commands that reproduce each one from the raw corpus. This file is the literal
output of `make audit`; nothing here is hand-written.

```

--- 1. cit_45a6c764f509  [raw_exact]
    opportunity: Weekly California Capacity Report, assembled and mailed by hand
    quote: "Transwestern's average deliveries to California were 1015 MMBtu/d (93%), with San Juan lateral throughput at 873 MMBtu/d."
    dd bs=1 skip=1339 count=121 if=corpus/lokay-m/sent_items/110. 2>/dev/null
    sed -n '23,23p' corpus/lokay-m/sent_items/110.

--- 2. cit_a99a1638e422  [raw_exact]
    opportunity: "Credit Report - 1/30/01" produced daily
    quote: "Subject: Credit Report--2/2/01"
    dd bs=1 skip=161 count=30 if=corpus/giron-d/sent/267. 2>/dev/null
    sed -n '5,5p' corpus/giron-d/sent/267.

--- 3. cit_70d1c123124d  [raw_exact]
    opportunity: "Calpine Daily Gas Nomination" produced monthly
    quote: "Subject: Calpine Daily Gas Nomination"
    dd bs=1 skip=158 count=37 if=corpus/farmer-d/logistics/1561. 2>/dev/null
    sed -n '5,5p' corpus/farmer-d/logistics/1561.

--- 4. cit_6ce9b034b132  [raw_exact]
    opportunity: Nomination changes confirmed by hand across Sitara, Unify and counterparties
    quote: "They said there is a chance they will have to do it again tomorrow."
    dd bs=1 skip=765 count=67 if=corpus/farmer-d/logistics/2108. 2>/dev/null
    sed -n '22,22p' corpus/farmer-d/logistics/2108.

--- 5. cit_b843b41c8654  [raw_exact]
    opportunity: "Calpine Daily Gas Nomination" produced monthly
    quote: "Subject: Calpine Daily Gas Nomination"
    dd bs=1 skip=152 count=37 if=corpus/farmer-d/logistics/1027. 2>/dev/null
    sed -n '5,5p' corpus/farmer-d/logistics/1027.

--- 6. cit_7959cb571714  [raw_exact]
    opportunity: Weekly California Capacity Report, assembled and mailed by hand
    quote: "Transwestern's average deliveries to California were 1122 MMBtu/d (103%), with San Juan lateral throughput at 844 MMBtu/d."
    dd bs=1 skip=1339 count=122 if=corpus/lokay-m/sent_items/18. 2>/dev/null
    sed -n '23,23p' corpus/lokay-m/sent_items/18.

--- 7. cit_c0504de3a61e  [raw_exact]
    opportunity: Extending deal tickets by hand to cover unallocated meter flow
    quote: "I am now on the dreaded ua4 list from Vol. Mgmt."
    dd bs=1 skip=886 count=48 if=corpus/farmer-d/logistics/1520. 2>/dev/null
    sed -n '24,24p' corpus/farmer-d/logistics/1520.

--- 8. cit_d0a4a6dca279  [raw_exact]
    opportunity: Monthly first-of-month gas nominations emailed in by counterparties
    quote: "revision PER JOHN KJELMYR, 12/26 am."
    dd bs=1 skip=964 count=36 if=corpus/farmer-d/logistics/2008. 2>/dev/null
    sed -n '34,34p' corpus/farmer-d/logistics/2008.

--- 9. cit_05652e64715e  [raw_exact]
    opportunity: Daily gas nominations mailed as Word and Excel attachments
    quote: "CALPINE DAILY GAS NOMINATION 1.doc"
    dd bs=1 skip=746 count=34 if=corpus/farmer-d/logistics/1318. 2>/dev/null
    sed -n '19,19p' corpus/farmer-d/logistics/1318.

--- 10. cit_feeabdbb4ec3  [raw_exact]
    opportunity: Weekly California Capacity Report, assembled and mailed by hand
    quote: "Sorry, the effective date for this new report is 01/07-01/11."
    dd bs=1 skip=1231 count=61 if=corpus/lokay-m/sent_items/46. 2>/dev/null
    sed -n '23,23p' corpus/lokay-m/sent_items/46.

--- 11. cit_58a2ebb7bf10  [raw_exact]
    opportunity: "Credit Report - 1/30/01" produced daily
    quote: "Subject: Credit Report--2/1/01"
    dd bs=1 skip=161 count=30 if=corpus/giron-d/sent/255. 2>/dev/null
    sed -n '5,5p' corpus/giron-d/sent/255.

--- 12. cit_8ce5472cc445  [raw_exact]
    opportunity: Monthly first-of-month gas nominations emailed in by counterparties
    quote: "Calpine January 2000 Nomination"
    dd bs=1 skip=166 count=31 if=corpus/farmer-d/logistics/619. 2>/dev/null
    sed -n '5,5p' corpus/farmer-d/logistics/619.

--- 13. cit_46ade1da95de  [rewrapped]
    opportunity: Nomination changes confirmed by hand across Sitara, Unify and counterparties
    quote: "a nom change from
3,300 to 2,400 mmbtu/d at HPL Meter 98-6296 delivery @ HPL Thompsonville"
    dd bs=1 skip=880 count=90 if=corpus/farmer-d/logistics/1151. 2>/dev/null
    sed -n '29,30p' corpus/farmer-d/logistics/1151.

--- 14. cit_5f7261c0f77a  [raw_exact]
    opportunity: Weekly California Capacity Report, assembled and mailed by hand
    quote: "Transwestern's average deliveries to California were 1058 MMBtu/d (97%), with San Juan lateral throughput at 864 MMBtu/d."
    dd bs=1 skip=1337 count=121 if=corpus/lokay-m/sent_items/79. 2>/dev/null
    sed -n '23,23p' corpus/lokay-m/sent_items/79.

--- 15. cit_f7716817d54d  [rewrapped]
    opportunity: Fixing wrong deal prices in Sitara after the fact
    quote: "please change and/or review a 
change of price for the Mar 15 item from $0.00000 to $7.20000 and advise when 
complete"
    dd bs=1 skip=666 count=118 if=corpus/giron-d/sent/57. 2>/dev/null
    sed -n '34,36p' corpus/giron-d/sent/57.

--- 16. cit_3251de1464be  [raw_exact]
    opportunity: Scheduled-versus-actual volume exceptions, reconciled by hand in Unify
    quote: "Why is nothing being allocated to Alpine?  This is a good deal we have in 
place with them and I really need the problem resolved."
    dd bs=1 skip=3046 count=130 if=corpus/farmer-d/logistics/2100. 2>/dev/null
    sed -n '78,79p' corpus/farmer-d/logistics/2100.

--- 17. cit_ecee0749008d  [raw_exact]
    opportunity: Fixing deal prices in Sitara by hand before invoices go out
    quote: "pls forward this to Daren so that he can change the price in Sitara to $ 5.235 +.05"
    dd bs=1 skip=889 count=83 if=corpus/farmer-d/logistics/179. 2>/dev/null
    sed -n '20,20p' corpus/farmer-d/logistics/179.

--- 18. cit_88fbca232748  [raw_exact]
    opportunity: Weekly California Capacity Report, assembled and mailed by hand
    quote: "Transwestern's average deliveries to California were 884 MMBtu/d (81%), with San Juan lateral throughput at 773 MMBtu/d."
    dd bs=1 skip=1333 count=120 if=corpus/lokay-m/inbox/32. 2>/dev/null
    sed -n '23,23p' corpus/lokay-m/inbox/32.

--- 19. cit_98bfe91399ac  [raw_exact]
    opportunity: Fixing deal prices in Sitara by hand before invoices go out
    quote: "Could you pls the pricing on this deal for March 2001 Production for days 25 & 26 to  $ 5.285?"
    dd bs=1 skip=1231 count=94 if=corpus/farmer-d/logistics/176. 2>/dev/null
    sed -n '36,36p' corpus/farmer-d/logistics/176.

--- 20. cit_61f81d3ab9f5  [raw_exact]
    opportunity: "Calpine Daily Gas Nomination" produced monthly
    quote: "Subject: Calpine Daily Gas Nomination"
    dd bs=1 skip=158 count=37 if=corpus/farmer-d/logistics/579. 2>/dev/null
    sed -n '5,5p' corpus/farmer-d/logistics/579.

--- 21. cit_52db8ac62baa  [raw_exact]
    opportunity: Fixing wrong deal prices in Sitara after the fact
    quote: "I changed the El Paso Electric deal #697528 price from $4 to $68. I should not receive the $25524.54 as revenue shown in the new deal summary."
    dd bs=1 skip=579 count=142 if=corpus/williams-w3/sent_items/366. 2>/dev/null
    sed -n '18,18p' corpus/williams-w3/sent_items/366.

--- 22. cit_4e2ac2d3f0d4  [raw_exact]
    opportunity: "Calpine Daily Gas Nomination" produced monthly
    quote: "Subject: Calpine Daily Gas Nomination"
    dd bs=1 skip=156 count=37 if=corpus/farmer-d/logistics/1411. 2>/dev/null
    sed -n '5,5p' corpus/farmer-d/logistics/1411.

--- 23. cit_24e03b2028aa  [raw_exact]
    opportunity: "Credit Report - 1/30/01" produced daily
    quote: "Subject: Credit Report--3/26/01"
    dd bs=1 skip=160 count=31 if=corpus/giron-d/sent/121. 2>/dev/null
    sed -n '5,5p' corpus/giron-d/sent/121.

--- 24. cit_da672f3158ef  [rewrapped]
    opportunity: Extending deal tickets by hand to cover unallocated meter flow
    quote: "I think that the deal needs to be extended, it looks like the valve 
was not completely shut by 9 am."
    dd bs=1 skip=701 count=101 if=corpus/farmer-d/logistics/1502. 2>/dev/null
    sed -n '22,23p' corpus/farmer-d/logistics/1502.

--- 25. cit_bd0c496a71cc  [rewrapped]
    opportunity: Extending deal tickets by hand to cover unallocated meter flow
    quote: "Please let me know if we want to extend this deal (85% 
of hsc - lg, etc) or if I should put this gas on Strangers until we determine 
what to do."
    dd bs=1 skip=738 count=146 if=corpus/farmer-d/logistics/1520. 2>/dev/null
    sed -n '22,24p' corpus/farmer-d/logistics/1520.


PASS  133 checks, 0 failures, 0 warnings
citation tiers: {'raw_exact': 65, 'rewrapped': 23}
```
