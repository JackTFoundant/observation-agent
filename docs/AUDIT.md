# Audit sample

25 citations chosen at random (seed 7) from the published report, with the
commands that reproduce each one from the raw corpus. This file is the literal
output of `make audit`; nothing here is hand-written.

```

--- 1. cit_d8ff0fa59bca  [rewrapped]
    opportunity: Mid-month nomination revisions re-keyed by hand for Josey and other meters
    quote: "Charlotte Hawkins is having trouble confirming the volume of 5,733 with El 
Paso."
    dd bs=1 skip=476 count=81 if=corpus/farmer-d/logistics/1163. 2>/dev/null
    sed -n '19,20p' corpus/farmer-d/logistics/1163.

--- 2. cit_c9e6e7fea071  [rewrapped]
    opportunity: Monthly nomination volume estimates agreed by email before month start
    quote: "Southern Union for May
2100 83 st
2100 Port Arthur"
    dd bs=1 skip=770 count=50 if=corpus/farmer-d/logistics/1056. 2>/dev/null
    sed -n '37,39p' corpus/farmer-d/logistics/1056.

--- 3. cit_ecee0749008d  [raw_exact]
    opportunity: Fixing deal prices in Sitara by hand, one email at a time
    quote: "pls forward this to Daren so that he can change the price in Sitara to $ 5.235 +.05"
    dd bs=1 skip=889 count=83 if=corpus/farmer-d/logistics/179. 2>/dev/null
    sed -n '20,20p' corpus/farmer-d/logistics/179.

--- 4. cit_b8eed68e3cff  [raw_exact]
    opportunity: Real-time West power position handoff notes to the next desk shift
    quote: "ST-WBOM is long at PV parking with PNM for HE 2 through HE 5, 20 mws each hour--for Friday and Saturday."
    dd bs=1 skip=555 count=104 if=corpus/williams-w3/sent_items/168. 2>/dev/null
    sed -n '19,19p' corpus/williams-w3/sent_items/168.

--- 5. cit_a99a1638e422  [raw_exact]
    opportunity: "Credit Report--5/9/01" produced daily
    quote: "Subject: Credit Report--2/2/01"
    dd bs=1 skip=161 count=30 if=corpus/giron-d/sent/267. 2>/dev/null
    sed -n '5,5p' corpus/giron-d/sent/267.

--- 6. cit_1fc812d3bfd7  [rewrapped]
    opportunity: Mid-month nomination revisions re-keyed by hand for Josey and other meters
    quote: "There has been a change for the Katy Plant.  First of the month nom is now 
expected to be 5,479 MMBtu/d."
    dd bs=1 skip=798 count=105 if=corpus/farmer-d/logistics/1467. 2>/dev/null
    sed -n '26,27p' corpus/farmer-d/logistics/1467.

--- 7. cit_d239579d3927  [raw_exact]
    opportunity: Extending existing deal tickets to cover unbooked meter flow
    quote: "Last deal used was 289396 could you extend it."
    dd bs=1 skip=598 count=46 if=corpus/farmer-d/logistics/2125. 2>/dev/null
    sed -n '20,20p' corpus/farmer-d/logistics/2125.

--- 8. cit_d73baaf8565e  [rewrapped]
    opportunity: Extending existing deal tickets to cover unbooked meter flow
    quote: "Could you extend this deal thru the 30th so that I 
can have Vol. Management create an accounting arrangement for it."
    dd bs=1 skip=548 count=117 if=corpus/farmer-d/logistics/1277. 2>/dev/null
    sed -n '18,19p' corpus/farmer-d/logistics/1277.

--- 9. cit_209530865957  [rewrapped]
    opportunity: Meter-level scheduled-versus-actual imbalance clearing across Unify, Sitara and HPL
    quote: "I sent Jackie Young an email 
back showing her TETCO's numbers and I haven't received a response."
    dd bs=1 skip=3360 count=97 if=corpus/farmer-d/logistics/1972. 2>/dev/null
    sed -n '62,63p' corpus/farmer-d/logistics/1972.

--- 10. cit_3d5781ebdb4e  [raw_exact]
    opportunity: Real-time West power position handoff notes to the next desk shift
    quote: "Please buy energy to cover this 15 mw short on Monday under the ST-WBOM book and sell to EPE at $0 under the ST-WBOM book."
    dd bs=1 skip=985 count=122 if=corpus/williams-w3/sent_items/380. 2>/dev/null
    sed -n '23,23p' corpus/williams-w3/sent_items/380.

--- 11. cit_88fbca232748  [raw_exact]
    opportunity: Weekly California Capacity Report, assembled and mailed by hand
    quote: "Transwestern's average deliveries to California were 884 MMBtu/d (81%), with San Juan lateral throughput at 773 MMBtu/d."
    dd bs=1 skip=1333 count=120 if=corpus/lokay-m/inbox/32. 2>/dev/null
    sed -n '23,23p' corpus/lokay-m/inbox/32.

--- 12. cit_8556efa92a71  [raw_exact]
    opportunity: Mid-month nomination revisions re-keyed by hand for Josey and other meters
    quote: "I went ahead and changed the volume 
down to 12,400 from 13,000."
    dd bs=1 skip=637 count=64 if=corpus/farmer-d/logistics/803. 2>/dev/null
    sed -n '19,20p' corpus/farmer-d/logistics/803.

--- 13. cit_281cdb8ece7c  [raw_exact]
    opportunity: "California Capacity Report for Week of 10/22-10/26" produced weekly
    quote: "Subject: California Capacity Report for Week of 01/21-01/25"
    dd bs=1 skip=323 count=59 if=corpus/lokay-m/sent_items/30. 2>/dev/null
    sed -n '8,8p' corpus/lokay-m/sent_items/30.

--- 14. cit_85be9a4dbc98  [raw_exact]
    opportunity: Mid-month nomination revisions re-keyed by hand for Josey and other meters
    quote: "Will you approve revising the volume in Unify down to 2,300?  Please advise."
    dd bs=1 skip=715 count=76 if=corpus/farmer-d/logistics/1163. 2>/dev/null
    sed -n '27,27p' corpus/farmer-d/logistics/1163.

--- 15. cit_f5accb55f956  [rewrapped]
    opportunity: Ad-hoc requests for system and deal-book access, by email
    quote: "was I supposed to send in 
another request for her and put it on Tom's Cost Center"
    dd bs=1 skip=503 count=82 if=corpus/farmer-d/logistics/1992. 2>/dev/null
    sed -n '17,18p' corpus/farmer-d/logistics/1992.

--- 16. cit_2cf730fe5eda  [rewrapped]
    opportunity: Moving deals between trading books by hand-run script requests
    quote: "I want to move all deals currently in the INTRA-EMWMEH book into the 
FT-IM-ENOV book."
    dd bs=1 skip=445 count=86 if=corpus/giron-d/sent/619. 2>/dev/null
    sed -n '19,20p' corpus/giron-d/sent/619.

--- 17. cit_4e2ac2d3f0d4  [raw_exact]
    opportunity: "Calpine Daily Gas Nomination" produced monthly
    quote: "Subject: Calpine Daily Gas Nomination"
    dd bs=1 skip=156 count=37 if=corpus/farmer-d/logistics/1411. 2>/dev/null
    sed -n '5,5p' corpus/farmer-d/logistics/1411.

--- 18. cit_82d1e31bd65b  [rewrapped]
    opportunity: Meter-level scheduled-versus-actual imbalance clearing across Unify, Sitara and HPL
    quote: "All the information that is supplied on the UA4 report is need a contract for 
9,448 MMBTU."
    dd bs=1 skip=1693 count=91 if=corpus/farmer-d/logistics/617. 2>/dev/null
    sed -n '46,47p' corpus/farmer-d/logistics/617.

--- 19. cit_e4720e85339e  [raw_exact]
    opportunity: Mid-month nomination revisions re-keyed by hand for Josey and other meters
    quote: "Here's REVISED February 2000 (effective 2/17/00 ) setup for Josey"
    dd bs=1 skip=897 count=65 if=corpus/farmer-d/logistics/800. 2>/dev/null
    sed -n '29,29p' corpus/farmer-d/logistics/800.

--- 20. cit_35837153d4d3  [raw_exact]
    opportunity: Ad-hoc requests for system and deal-book access, by email
    quote: "I don't believe I am set up to review as a supervisor in the PEP system.  How 
do I get this changed in the system?"
    dd bs=1 skip=447 count=115 if=corpus/giron-d/sent/789. 2>/dev/null
    sed -n '18,19p' corpus/giron-d/sent/789.

--- 21. cit_31f1fd31b136  [raw_exact]
    opportunity: "Credit Report--5/9/01" produced daily
    quote: "Subject: Credit Report--2/15/01"
    dd bs=1 skip=162 count=31 if=corpus/giron-d/sent/220. 2>/dev/null
    sed -n '5,5p' corpus/giron-d/sent/220.

--- 22. cit_0b31e2ddac2b  [raw_exact]
    opportunity: Mid-month nomination revisions re-keyed by hand for Josey and other meters
    quote: "Prize Energy revised their nom eff. 6/26 through 6/29 for the following 
meters:"
    dd bs=1 skip=455 count=80 if=corpus/farmer-d/logistics/1239. 2>/dev/null
    sed -n '19,20p' corpus/farmer-d/logistics/1239.

--- 23. cit_58a2ebb7bf10  [raw_exact]
    opportunity: "Credit Report--5/9/01" produced daily
    quote: "Subject: Credit Report--2/1/01"
    dd bs=1 skip=161 count=30 if=corpus/giron-d/sent/255. 2>/dev/null
    sed -n '5,5p' corpus/giron-d/sent/255.

--- 24. cit_062d4ac5876c  [raw_exact]
    opportunity: Monthly nomination volume estimates agreed by email before month start
    quote: "5031 at TVille I-.02 for May"
    dd bs=1 skip=787 count=28 if=corpus/farmer-d/logistics/1057. 2>/dev/null
    sed -n '35,35p' corpus/farmer-d/logistics/1057.

--- 25. cit_a571de3d3430  [raw_exact]
    opportunity: Monthly meter volume figures passed by hand to schedulers
    quote: "Meter 6722 (not sure if you need this) - Julie"
    dd bs=1 skip=552 count=46 if=corpus/farmer-d/logistics/153. 2>/dev/null
    sed -n '17,17p' corpus/farmer-d/logistics/153.


PASS  165 checks, 0 failures, 0 warnings
citation tiers: {'raw_exact': 85, 'rewrapped': 26, 'decoded_exact': 1}
```
