import csv

TEMPLATE = '''<li>
  <div class='listing-name'>{name}</div>
  <div>{address}</div>
  <div>{city}, {state}</div>
  <a href="tel:{phone}">{phone}</a>
</li>'''

with open('listings.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    if not row['Business Name']:
      continue
    print TEMPLATE.format(
      name=row['Business Name'],
      address=row['Street Address'],
      city=row['City '],
      state=row['State'],
      phone=row['Phone Number']
    )
