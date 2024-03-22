# blocknolu
- The `build_geo_table.py` can build pf tables or cisco extended access list (I haven't tested the cisco part though, so i'd appreciate some feedback / PR if needed).
- It can build tables for most country codes plus benelux, and europe:
  - `benelux = ["lu", "be", "nl"]`
  - `eu = ["at", "be", "bg", "hr", "cy", "cz", "dk", "ee", "fi", "fr", "de", "gr", "hu", "ie", "it", "lv" ,"lt", "lu", "mt", "nl", "pl", "pt", "ro", "sk", "si", "es", "se"]` 
- Beware that in addition to the tables generated, the script adds the following expressions:
```bash
block in
pass out
pass in from <country_ips> to any
```

# Installation
In a linux system with python3, install the requirements in a virtual environments:
```bash
python3 -venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

# Use
```bash
python3 ./build_geo_table.py --help
Usage: build_geo_table.py [OPTIONS]

Options:
  --country [eu|benelux|ad|ae|af|ag|ai|al|am|ao|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bl|bm|bn|bo|bq|br|bs|bt|bw|by|bz|ca|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cu|cv|cw|cy|cz|de|dj|dk|dm|do|dz|ec|ee|eg|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gt|gu|gw|gy|hk|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mf|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|si|sk|sl|sm|sn|so|sr|ss|st|sv|sx|sy|sz|tc|td|tg|th|tj|tk|tl|tm|tn|to|tr|tt|tv|tw|tz|ua|ug|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|za|zm|zw]
                                  Specify the country code for which you want
                                  to create a table, or benelux, or eu.
                                  [required]
  --format [pf|cisco]             Specify the format of the output. Default is
                                  pf.
  --help                          Show this message and exit.
```

# Licence
    Copyright (C) 2024 Jean-Louis Huynen

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.