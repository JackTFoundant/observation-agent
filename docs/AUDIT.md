# Audit sample

25 citations chosen at random (seed 7) from the published report, with the
commands that reproduce each one from the raw corpus. This file is the literal
output of `make audit`; nothing here is hand-written.

```

--- 1. cit_70d1c123124d  [raw_exact]
    opportunity: "Calpine Daily Gas Nomination" produced monthly
    quote: "Subject: Calpine Daily Gas Nomination"
    dd bs=1 skip=158 count=37 if=corpus/farmer-d/logistics/1561. 2>/dev/null
    sed -n '5,5p' corpus/farmer-d/logistics/1561.

--- 2. cit_feeabdbb4ec3  [raw_exact]
    opportunity: Weekly California Capacity Report, assembled and mailed by hand
    quote: "Sorry, the effective date for this new report is 01/07-01/11."
    dd bs=1 skip=1231 count=61 if=corpus/lokay-m/sent_items/46. 2>/dev/null
    sed -n '23,23p' corpus/lokay-m/sent_items/46.

--- 3. cit_61f81d3ab9f5  [raw_exact]
    opportunity: "Calpine Daily Gas Nomination" produced monthly
    quote: "Subject: Calpine Daily Gas Nomination"
    dd bs=1 skip=158 count=37 if=corpus/farmer-d/logistics/579. 2>/dev/null
    sed -n '5,5p' corpus/farmer-d/logistics/579.

--- 4. cit_a99a1638e422  [raw_exact]
    opportunity: "Credit Report - 1/30/01" produced daily
    quote: "Subject: Credit Report--2/2/01"
    dd bs=1 skip=161 count=30 if=corpus/giron-d/sent/267. 2>/dev/null
    sed -n '5,5p' corpus/giron-d/sent/267.

--- 5. cit_b062780bfa12  [raw_exact]
    opportunity: Enovate daily position report (DPR), circulated by hand for approval
    quote: "Prelim Enovate DPR for 2/14/2001"
    dd bs=1 skip=178 count=32 if=corpus/giron-d/sent/221. 2>/dev/null
    sed -n '5,5p' corpus/giron-d/sent/221.

--- 6. cit_9f0498ab829a  [rewrapped]
    opportunity: Extending Sitara deals by request to cover unallocated meter flow
    quote: "The East Desk was not up and 
running on Unify in June of 1999.  All of our pathing for June of 1999 was in 
Autonoms and it's not y2K compatabile."
    dd bs=1 skip=976 count=147 if=corpus/farmer-d/logistics/1489. 2>/dev/null
    sed -n '25,27p' corpus/farmer-d/logistics/1489.

--- 7. cit_b843b41c8654  [raw_exact]
    opportunity: "Calpine Daily Gas Nomination" produced monthly
    quote: "Subject: Calpine Daily Gas Nomination"
    dd bs=1 skip=152 count=37 if=corpus/farmer-d/logistics/1027. 2>/dev/null
    sed -n '5,5p' corpus/farmer-d/logistics/1027.

--- 8. cit_0c3312966342  [rewrapped]
    opportunity: Meter-level scheduled-vs-actual volume reconciliation, chased by email
    quote: "it seems odd to me that scheduling had 8,928 
MMBtu confirmed at this point and only 646 MMBtu flowed."
    dd bs=1 skip=1436 count=102 if=corpus/farmer-d/logistics/2100. 2>/dev/null
    sed -n '36,37p' corpus/farmer-d/logistics/2100.

--- 9. cit_d6681d88e310  [raw_exact]
    opportunity: Weekly California Capacity Report, assembled and mailed by hand
    quote: "Transwestern's average deliveries to California were 855 MMBtu/d (79%), with San Juan lateral throughput at 839 MMBtu/d."
    dd bs=1 skip=1343 count=120 if=corpus/lokay-m/sent_items/47. 2>/dev/null
    sed -n '23,23p' corpus/lokay-m/sent_items/47.

--- 10. cit_a1667ea29fa2  [raw_exact]
    opportunity: Correcting mispriced deals by hand in Sitara after the fact
    quote: "Deal 819592 - the commodity price needs to be 3.6318"
    dd bs=1 skip=708 count=52 if=corpus/farmer-d/logistics/74. 2>/dev/null
    sed -n '22,22p' corpus/farmer-d/logistics/74.

--- 11. cit_900f67bebeae  [raw_exact]
    opportunity: Daily gas nominations mailed as attached Word and Excel files
    quote: "HPL Nom for January 4, 2001"
    dd bs=1 skip=313 count=27 if=corpus/farmer-d/logistics/2025. 2>/dev/null
    sed -n '7,7p' corpus/farmer-d/logistics/2025.

--- 12. cit_da672f3158ef  [rewrapped]
    opportunity: Extending Sitara deals by request to cover unallocated meter flow
    quote: "I think that the deal needs to be extended, it looks like the valve 
was not completely shut by 9 am."
    dd bs=1 skip=701 count=101 if=corpus/farmer-d/logistics/1502. 2>/dev/null
    sed -n '22,23p' corpus/farmer-d/logistics/1502.

--- 13. cit_58a2ebb7bf10  [raw_exact]
    opportunity: "Credit Report - 1/30/01" produced daily
    quote: "Subject: Credit Report--2/1/01"
    dd bs=1 skip=161 count=30 if=corpus/giron-d/sent/255. 2>/dev/null
    sed -n '5,5p' corpus/giron-d/sent/255.

--- 14. cit_87bf115002e9  [raw_exact]
    opportunity: Daily gas nominations mailed as attached Word and Excel files
    quote: "(See attached file: egmnom-Feb.xls)"
    dd bs=1 skip=840 count=35 if=corpus/farmer-d/logistics/767. 2>/dev/null
    sed -n '31,31p' corpus/farmer-d/logistics/767.

--- 15. cit_4e2ac2d3f0d4  [raw_exact]
    opportunity: "Calpine Daily Gas Nomination" produced monthly
    quote: "Subject: Calpine Daily Gas Nomination"
    dd bs=1 skip=156 count=37 if=corpus/farmer-d/logistics/1411. 2>/dev/null
    sed -n '5,5p' corpus/farmer-d/logistics/1411.

--- 16. cit_d7d7daa00d35  [raw_exact]
    opportunity: Monthly first-of-month gas nominations mailed in by plant customers
    quote: "Below are Forest's first of the month noms:"
    dd bs=1 skip=815 count=43 if=corpus/farmer-d/logistics/2008. 2>/dev/null
    sed -n '27,27p' corpus/farmer-d/logistics/2008.

--- 17. cit_e474f470ba47  [raw_exact]
    opportunity: "California Capacity Report for Week of 01/14-01/18" produced weekly
    quote: "Subject: California Capacity Report for Week of 12/17-12/21"
    dd bs=1 skip=325 count=59 if=corpus/lokay-m/sent_items/67. 2>/dev/null
    sed -n '8,8p' corpus/lokay-m/sent_items/67.

--- 18. cit_d0a4a6dca279  [raw_exact]
    opportunity: Monthly first-of-month gas nominations mailed in by plant customers
    quote: "revision PER JOHN KJELMYR, 12/26 am."
    dd bs=1 skip=964 count=36 if=corpus/farmer-d/logistics/2008. 2>/dev/null
    sed -n '34,34p' corpus/farmer-d/logistics/2008.

--- 19. cit_88fbca232748  [raw_exact]
    opportunity: Weekly California Capacity Report, assembled and mailed by hand
    quote: "Transwestern's average deliveries to California were 884 MMBtu/d (81%), with San Juan lateral throughput at 773 MMBtu/d."
    dd bs=1 skip=1333 count=120 if=corpus/lokay-m/inbox/32. 2>/dev/null
    sed -n '23,23p' corpus/lokay-m/inbox/32.

--- 20. cit_859399dded08  [raw_exact]
    opportunity: Fixing miskeyed Sitara deal entries after the fact
    quote: "Aquila split the volume between two points, that is why the deal changed."
    dd bs=1 skip=568 count=73 if=corpus/farmer-d/logistics/1303. 2>/dev/null
    sed -n '24,24p' corpus/farmer-d/logistics/1303.

--- 21. cit_04eb86a692b1  [rewrapped]
    opportunity: Monthly first-of-month gas nominations mailed in by plant customers
    quote: "This is the estimated Josey Ranch nomination for the month of April
2000."
    dd bs=1 skip=1013 count=73 if=corpus/farmer-d/logistics/993. 2>/dev/null
    sed -n '30,31p' corpus/farmer-d/logistics/993.

--- 22. cit_2a00ab6ddeb5  [raw_exact]
    opportunity: Daily gas nominations mailed as attached Word and Excel files
    quote: "Confirmed on my end. Same volumes as yesterday, no changes to the path."
    dd bs=1 skip=452 count=71 if=corpus/giron-d/sent/795. 2>/dev/null
    sed -n '16,16p' corpus/giron-d/sent/795.

--- 23. cit_3251de1464be  [rewrapped]
    opportunity: Meter-level scheduled-vs-actual volume reconciliation, chased by email
    quote: "Why is nothing being allocated to Alpine?  This is a good deal we have in 
place with them and I really need the problem resolved."
    dd bs=1 skip=3046 count=130 if=corpus/farmer-d/logistics/2100. 2>/dev/null
    sed -n '78,79p' corpus/farmer-d/logistics/2100.

--- 24. cit_45a6c764f509  [raw_exact]
    opportunity: Weekly California Capacity Report, assembled and mailed by hand
    quote: "Transwestern's average deliveries to California were 1015 MMBtu/d (93%), with San Juan lateral throughput at 873 MMBtu/d."
    dd bs=1 skip=1339 count=121 if=corpus/lokay-m/sent_items/110. 2>/dev/null
    sed -n '23,23p' corpus/lokay-m/sent_items/110.

--- 25. cit_24e03b2028aa  [raw_exact]
    opportunity: "Credit Report - 1/30/01" produced daily
    quote: "Subject: Credit Report--3/26/01"
    dd bs=1 skip=160 count=31 if=corpus/giron-d/sent/121. 2>/dev/null
    sed -n '5,5p' corpus/giron-d/sent/121.


PASS  137 checks, 0 failures, 0 warnings
citation tiers: {'raw_exact': 60, 'rewrapped': 28, 'decoded_exact': 1}
```
