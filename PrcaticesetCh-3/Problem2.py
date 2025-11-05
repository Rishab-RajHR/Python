# Replace name and date

letter =  ''' Dear <|Name|>,
              You are selected!
              <|Date|>'''

print(letter.replace("<|Name|>", "Alex").replace("<|Date|>", "24 October 2025"))