# Audit sample

25 citations chosen at random (seed 7) from the published report, with the
commands that reproduce each one from the raw corpus. This file is the literal
output of `make audit`; nothing here is hand-written.

```

--- 1. cit_d8ff0fa59bca  [rewrapped]
    opportunity: Mid-month nomination revisions re-keyed by hand for Josey, Katy and El Paso
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
    opportunity: Sitara deal price corrections requested by email
    quote: "pls forward this to Daren so that he can change the price in Sitara to $ 5.235 +.05"
    dd bs=1 skip=889 count=83 if=corpus/farmer-d/logistics/179. 2>/dev/null
    sed -n '20,20p' corpus/farmer-d/logistics/179.

--- 4. cit_76251f7744e6  [raw_exact]
    opportunity: Real-time West power desk shift handoff and booking instructions by email
    quote: "These pieces will need to be scheduled with the APX as the counterparty for HE 12-20."
    dd bs=1 skip=1576 count=85 if=corpus/williams-w3/sent_items/405. 2>/dev/null
    sed -n '27,27p' corpus/williams-w3/sent_items/405.

--- 5. cit_a99a1638e422  [raw_exact]
    opportunity: "Credit Report - 1/30/01" produced daily
    quote: "Subject: Credit Report--2/2/01"
    dd bs=1 skip=161 count=30 if=corpus/giron-d/sent/267. 2>/dev/null
    sed -n '5,5p' corpus/giron-d/sent/267.

--- 6. cit_1fc812d3bfd7  [rewrapped]
    opportunity: Mid-month nomination revisions re-keyed by hand for Josey, Katy and El Paso
    quote: "There has been a change for the Katy Plant.  First of the month nom is now 
expected to be 5,479 MMBtu/d."
    dd bs=1 skip=798 count=105 if=corpus/farmer-d/logistics/1467. 2>/dev/null
    sed -n '26,27p' corpus/farmer-d/logistics/1467.

--- 7. cit_9f0498ab829a  [rewrapped]
    opportunity: Extending existing deal tickets in Sitara/Unify to cover unbooked meter flow
    quote: "The East Desk was not up and 
running on Unify in June of 1999.  All of our pathing for June of 1999 was in 
Autonoms and it's not y2K compatabile."
    dd bs=1 skip=976 count=147 if=corpus/farmer-d/logistics/1489. 2>/dev/null
    sed -n '25,27p' corpus/farmer-d/logistics/1489.

--- 8. cit_9e9ab1d61248  [rewrapped]
    opportunity: Extending existing deal tickets in Sitara/Unify to cover unbooked meter flow
    quote: "Is this date really June of 1999?  Hopefully we're not just finding out about 
this?"
    dd bs=1 skip=1357 count=84 if=corpus/farmer-d/logistics/1492. 2>/dev/null
    sed -n '38,39p' corpus/farmer-d/logistics/1492.

--- 9. cit_209530865957  [rewrapped]
    opportunity: Meter-level scheduled-vs-actual variance clearing across Unify, Sitara and UA4
    quote: "I sent Jackie Young an email 
back showing her TETCO's numbers and I haven't received a response."
    dd bs=1 skip=3360 count=97 if=corpus/farmer-d/logistics/1972. 2>/dev/null
    sed -n '62,63p' corpus/farmer-d/logistics/1972.

--- 10. cit_3d5781ebdb4e  [raw_exact]
    opportunity: Real-time West power desk shift handoff and booking instructions by email
    quote: "Please buy energy to cover this 15 mw short on Monday under the ST-WBOM book and sell to EPE at $0 under the ST-WBOM book."
    dd bs=1 skip=985 count=122 if=corpus/williams-w3/sent_items/380. 2>/dev/null
    sed -n '23,23p' corpus/williams-w3/sent_items/380.

--- 11. cit_e142f4dedf42  [raw_exact]
    opportunity: Weekly California Capacity Report, assembled and mailed by hand
    quote: "Transwestern's average deliveries to California were 959 MMBtu/d (88%), with San Juan lateral throughput at 827 MMBtu/d."
    dd bs=1 skip=1338 count=120 if=corpus/lokay-m/sent_items/63. 2>/dev/null
    sed -n '23,23p' corpus/lokay-m/sent_items/63.

--- 12. cit_9a011bdc98a6  [rewrapped]
    opportunity: Mid-month nomination revisions re-keyed by hand for Josey, Katy and El Paso
    quote: "This change is for the last two days of the month of March (I am sending a
day earlier than normal deadline because I'm getting covered up with April!)"
    dd bs=1 skip=938 count=151 if=corpus/farmer-d/logistics/984. 2>/dev/null
    sed -n '31,32p' corpus/farmer-d/logistics/984.

--- 13. cit_281cdb8ece7c  [raw_exact]
    opportunity: "California Capacity Report for Week of 01/14-01/18" produced weekly
    quote: "Subject: California Capacity Report for Week of 01/21-01/25"
    dd bs=1 skip=323 count=59 if=corpus/lokay-m/sent_items/30. 2>/dev/null
    sed -n '8,8p' corpus/lokay-m/sent_items/30.

--- 14. cit_85be9a4dbc98  [raw_exact]
    opportunity: Mid-month nomination revisions re-keyed by hand for Josey, Katy and El Paso
    quote: "Will you approve revising the volume in Unify down to 2,300?  Please advise."
    dd bs=1 skip=715 count=76 if=corpus/farmer-d/logistics/1163. 2>/dev/null
    sed -n '27,27p' corpus/farmer-d/logistics/1163.

--- 15. cit_f5accb55f956  [rewrapped]
    opportunity: Ad-hoc requests for system and deal-book access, by email
    quote: "was I supposed to send in 
another request for her and put it on Tom's Cost Center"
    dd bs=1 skip=503 count=82 if=corpus/farmer-d/logistics/1992. 2>/dev/null
    sed -n '17,18p' corpus/farmer-d/logistics/1992.

--- 16. cit_ac1079e9161a  [raw_exact]
    opportunity: Moving deals between trading books by hand-run script requests
    quote: "If I can have all the answers soon then I think the deals move can be completed around 3:00p.m."
    dd bs=1 skip=1166 count=95 if=corpus/giron-d/inbox/67. 2>/dev/null
    sed -n '29,29p' corpus/giron-d/inbox/67.

--- 17. cit_4e2ac2d3f0d4  [raw_exact]
    opportunity: "Calpine Daily Gas Nomination" produced monthly
    quote: "Subject: Calpine Daily Gas Nomination"
    dd bs=1 skip=156 count=37 if=corpus/farmer-d/logistics/1411. 2>/dev/null
    sed -n '5,5p' corpus/farmer-d/logistics/1411.

--- 18. cit_b4d145322843  [rewrapped]
    opportunity: Meter-level scheduled-vs-actual variance clearing across Unify, Sitara and UA4
    quote: "scheduling had 8,928 
MMBtu confirmed at this point and only 646 MMBtu flowed"
    dd bs=1 skip=1460 count=77 if=corpus/farmer-d/logistics/2100. 2>/dev/null
    sed -n '36,37p' corpus/farmer-d/logistics/2100.

--- 19. cit_e4720e85339e  [raw_exact]
    opportunity: Mid-month nomination revisions re-keyed by hand for Josey, Katy and El Paso
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
    opportunity: "Credit Report - 1/30/01" produced daily
    quote: "Subject: Credit Report--2/15/01"
    dd bs=1 skip=162 count=31 if=corpus/giron-d/sent/220. 2>/dev/null
    sed -n '5,5p' corpus/giron-d/sent/220.

--- 22. cit_0b31e2ddac2b  [raw_exact]
    opportunity: Mid-month nomination revisions re-keyed by hand for Josey, Katy and El Paso
    quote: "Prize Energy revised their nom eff. 6/26 through 6/29 for the following 
meters:"
    dd bs=1 skip=455 count=80 if=corpus/farmer-d/logistics/1239. 2>/dev/null
    sed -n '19,20p' corpus/farmer-d/logistics/1239.

--- 23. cit_58a2ebb7bf10  [raw_exact]
    opportunity: "Credit Report - 1/30/01" produced daily
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
