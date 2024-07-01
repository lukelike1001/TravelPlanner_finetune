import csv
import re

# Sample input string
input_string = """
                                     Name  Latitude  Longitude                                         Address          Phone                                                                                           Website   City
                The Dallas World Aquarium 32.783474 -96.805358        1801 N Griffin St, Dallas, TX 75202, USA (214) 720-2224                                                                           https://www.dwazoo.com/ Dallas
   The Sixth Floor Museum at Dealey Plaza 32.779819 -96.808484               411 Elm St, Dallas, TX 75202, USA (214) 747-6660                                                                              https://www.jfk.org/ Dallas
                            Reunion Tower 32.775506 -96.808857       300 Reunion Blvd E, Dallas, TX 75207, USA (214) 296-9950                                                                      http://www.reuniontower.com/ Dallas
                     Dallas Museum of Art 32.787696 -96.801044        1717 N Harwood St, Dallas, TX 75201, USA (214) 922-1200                                                                              https://www.dma.org/ Dallas
The Dallas Arboretum and Botanical Garden 32.823618 -96.716624          8525 Garland Rd, Dallas, TX 75218, USA (214) 515-6615                                                                  https://www.dallasarboretum.org/ Dallas
                               Dallas Zoo 32.740970 -96.815320  650 S R.L. Thornton Fwy, Dallas, TX 75203, USA (469) 554-7501                                                                        https://www.dallaszoo.com/ Dallas
                        Klyde Warren Park 32.789364 -96.801618 2012 Woodall Rodgers Fwy, Dallas, TX 75201, USA (214) 716-4500                                                                       http://klydewarrenpark.org/ Dallas
                            Old City Park 32.772753 -96.786544        1515 S Harwood St, Dallas, TX 75215, USA (214) 421-5141                                                                 http://www.oldcityparkdallas.org/ Dallas
       Perot Museum of Nature and Science 32.786943 -96.806584          2201 N Field St, Dallas, TX 75201, USA (214) 428-5555                                                                      https://www.perotmuseum.org/ Dallas
                            Pioneer Plaza 32.776632 -96.801199            1428 Young St, Dallas, TX 75202, USA        Unknown                          http://www.dallasparks.org/Facilities/Facility/Details/Pioneer-Plaza-624 Dallas
                  Nasher Sculpture Center 32.788182 -96.800157            2001 Flora St, Dallas, TX 75201, USA (214) 242-5100                                                             http://www.nashersculpturecenter.org/ Dallas
                            Giant Eyeball 32.781406 -96.798312             1601 Main St, Dallas, TX 75201, USA        Unknown https://artandseek.org/2021/03/18/why-is-there-a-giant-eyeball-in-downtown-dallas-we-take-a-look/ Dallas
           John F. Kennedy Memorial Plaza 32.778725 -96.806451              646 Main St, Dallas, TX 75202, USA (214) 747-6660                                                https://www.jfk.org/john-f-kennedy-memorial-plaza/ Dallas
                             Dealey Plaza 32.778818 -96.808299                           Dallas, TX 75202, USA (214) 670-4100                           http://www.dallasparks.org/Facilities/Facility/Details/Dealey-Plaza-462 Dallas
        African American Museum of Dallas 32.779057 -96.764414           3536 Grand Ave, Dallas, TX 75210, USA (214) 565-9026                                                                         http://www.aamdallas.org/ Dallas
               Frontiers of Flight Museum 32.842602 -96.835202          6911 Lemmon Ave, Dallas, TX 75209, USA (214) 350-3600                                                                      http://www.flightmuseum.com/ Dallas
                     White Rock Lake Park 32.836514 -96.721612        8300 E Lawther Dr, Dallas, TX 75218, USA (214) 660-1100                                                                     http://www.whiterocklake.org/ Dallas
             Leonhardt Lagoon Nature Walk 32.777830 -96.761946             1121 1st Ave, Dallas, TX 75210, USA (214) 426-3400                                  https://eventseeker.com/venue/1132302-leonhardt-lagoon-dallas-tx Dallas
       George W. Bush Presidential Center 32.841183 -96.778198       2943 SMU Boulevard, Dallas, TX 75205, USA (214) 200-4300                                                                        http://www.bushcenter.org/ Dallas
            Trinity Forest Adventure Park 32.689810 -96.675766      1800 Dowdy Ferry Rd, Dallas, TX 75217, USA (214) 391-1000                                                                       http://trinitytreetops.com/ Dallas
Restaurants in Dallas
                       Name  Average Cost                                               Cuisines  Aggregate Rating   City
         Coconuts Fish Cafe            38                    Cafe, BBQ, Mediterranean, Fast Food               4.5 Dallas
        1918 Bistro & Grill            90                               Tea, Pizza, BBQ, Seafood               4.4 Dallas
             Yanki Sizzlers            96                       Cafe, French, Tea, Mediterranean               4.1 Dallas
               Aravali Owls            53                Pizza, Italian, Bakery, Fast Food, Cafe               0.0 Dallas
               Kebab Xpress            93                      Tea, Bakery, Pizza, Mediterranean               2.7 Dallas
                 Haldiram"s            94                                             Tea, Pizza               3.6 Dallas
                  Delhicacy            67            Desserts, Mexican, Bakery, Chinese, Seafood               3.8 Dallas
                    L"Opera            77                French, Bakery, BBQ, Fast Food, Seafood               3.8 Dallas
            Cafe Gatherings            17                               Bakery, Indian, Desserts               4.4 Dallas
              Drifters Cafe            21                    Tea, French, Mexican, Cafe, Seafood               3.9 Dallas
           Uma Foodies" Hut            49                                French, Bakery, Seafood               3.1 Dallas
Belfrance Luxury Chocolates            96             Desserts, Pizza, Fast Food, Cafe, American               4.4 Dallas
                Puri Bakers            33        Pizza, Mexican, Bakery, Fast Food, Cafe, Indian               3.7 Dallas
             Bikaner Sweets            23                     Tea, French, Bakery, Cafe, Seafood               3.3 Dallas
            Metro Fast Food            45             Tea, Pizza, Mexican, Bakery, BBQ, American               2.7 Dallas
                    Wheelyz            60        Tea, Pizza, Bakery, BBQ, Chinese, Mediterranean               2.5 Dallas
              R. Ahmad Food            58 Desserts, Bakery, BBQ, Chinese, Mediterranean, Seafood               3.0 Dallas
                   Castle 9            32        Mexican, Bakery, BBQ, Fast Food, Cafe, American               3.1 Dallas
               Cafe Hawkers            72                                    Bakery, Indian, BBQ               3.7 Dallas
              Firefly India            87                        Cafe, Bakery, American, Italian               3.4 Dallas
            Zaaika Junction            48                                      Desserts, Seafood               2.6 Dallas
                  Papa Buns            75                       French, Pizza, Indian, Fast Food               0.0 Dallas
                TiffinToons            99            Seafood, Mediterranean, Desserts, Fast Food               0.0 Dallas
               Mamma Drools            45           BBQ, Fast Food, Cafe, Mediterranean, Seafood               0.0 Dallas
                 McDonald"s            56                                          Cafe, Seafood               3.5 Dallas
            Cafe Coffee Day            76                           Fast Food, Desserts, Italian               2.9 Dallas
                   Hardwari            28               Desserts, Tea, Pizza, Mexican, Fast Food               0.0 Dallas
               Baker"s Stop            69                Cafe, American, Mediterranean, Desserts               3.8 Dallas
          Delhi Biryani Hut            90                               Pizza, American, Seafood               0.0 Dallas
             Tikka Junction            86  Tea, Bakery, Fast Food, Cafe, American, Mediterranean               3.5 Dallas
            Nutrition Theka            77                             Pizza, American, Fast Food               3.3 Dallas
               Relax Xpress            53           Desserts, Pizza, Bakery, Cafe, Mediterranean               3.2 Dallas
              Lodhi Knights            18                       Tea, Pizza, French, Bakery, Cafe               3.1 Dallas
           Tandoori Khazana            61              Tea, Pizza, BBQ, Chinese, Indian, Seafood               0.0 Dallas
                Madras Cafe            90                     Bakery, Pizza, American, Fast Food               0.0 Dallas
                  Bake Club           100                       Cafe, Indian, Mediterranean, BBQ               3.1 Dallas
                   Yo Tibet            96         Desserts, Pizza, BBQ, Chinese, Indian, Seafood               3.3 Dallas
                 The Kahuna            23                          Bakery, Pizza, BBQ, Fast Food               3.1 Dallas
            Cafe Hera Pheri            18                                         Cafe, Desserts               3.8 Dallas
  Chanana Ice Cream Parlour            77                           Chinese, Pizza, BBQ, Italian               2.9 Dallas
               Dilli Darbar            64                      Tea, Cafe, Mediterranean, Italian               3.3 Dallas
     New Tayal"s Restaurant            67                        Mexican, Bakery, BBQ, Fast Food               2.8 Dallas
              Subs n Shakes            74                 French, Bakery, Mediterranean, Seafood               3.1 Dallas
                 Soya Grill            84                            Cafe, Pizza, BBQ, Fast Food               3.0 Dallas
             Bikaner Sweets            33                        Bakery, Pizza, Indian, Desserts               0.0 Dallas
                     Scoops            76                       Tea, Chinese, Seafood, Fast Food               2.8 Dallas
              Food N Shakes            23                  Desserts, Pizza, French, BBQ, Seafood               0.0 Dallas
              Cake Knighter            95     Pizza, Fast Food, American, Mediterranean, Seafood               0.0 Dallas
            Cafe Coffee Day            22                           Cafe, BBQ, Desserts, Seafood               3.0 Dallas
            Sona Restaurant            47                            Tea, Cafe, Pizza, Fast Food               3.2 Dallas
           Pirates of Grill            72                   Desserts, Italian, BBQ, Bakery, Cafe               3.9 Dallas
    Aim Cafe And Restaurant            85                                       Tea, French, BBQ               3.3 Dallas
             Wich "N" Shake            31                  Tea, Mexican, Bakery, Fast Food, Cafe               0.0 Dallas
      Kolkata Biryani House            11                     Tea, French, Cafe, Indian, Seafood               2.8 Dallas
          Flames of Tandoor            57                      Tea, Chinese, Desserts, Fast Food               3.5 Dallas
                 Shahenshah            92                       Fast Food, Seafood, BBQ, Italian               3.5 Dallas
                   MS Foods            55                                   Cafe, Pizza, Italian               3.1 Dallas
               Food Weavers            71             Tea, Bakery, BBQ, Fast Food, Mediterranean               0.0 Dallas
             The Grill @ 76            51                                         BBQ, Fast Food               3.5 Dallas
                      MONKS            24               Tea, Pizza, Cafe, Mediterranean, Seafood               4.2 Dallas
        Salsa Mexican Grill            63                  Desserts, BBQ, Bakery, Cafe, American               4.3 Dallas
                Dem Karak韄y            44                                       Pizza, Fast Food               4.5 Dallas
Accommodations in Dallas
                                            NAME  price       room type                                     house_rules  minimum nights  maximum occupancy  review rate number   city
                1BR, elevator, kitchen, doorman!  475.0 Entire home/apt                                      No parties             1.0                  3                 2.0 Dallas
Luxury Williamsburg duplex, private roof terrace  241.0 Entire home/apt                                     No visitors             4.0                  3                 5.0 Dallas
               Take it now you won"t find better  609.0 Entire home/apt                                         No pets             1.0                  4                 2.0 Dallas
              E. W"burg Private Room near subway  272.0    Private room                        No visitors & No smoking            15.0                  2                 2.0 Dallas
  Cozy&Central:EmpireState/Highline/Times Square  628.0 Entire home/apt              No visitors & No pets & No smoking             3.0                  4                 3.0 Dallas
                              *Fresh Budget Room  262.0    Private room                        No visitors & No smoking             2.0                  1                 4.0 Dallas
                   Chic Union Square One Bedroom 1096.0 Entire home/apt                                     No visitors             3.0                  5                 5.0 Dallas
    Bright and modern apartment in Williamsburg!  865.0 Entire home/apt                                      No smoking             6.0                  5                 4.0 Dallas
              Jackson Heights 2 bedrooms housing  747.0 Entire home/apt  No parties & No children under 10 & No smoking             2.0                  2                 3.0 Dallas
            Exclusive Modern Penthouse Apartment  483.0 Entire home/apt                           No pets & No visitors             1.0                  3                 3.0 Dallas
  SUNNY, SAFE and FRIENDLY minutes to Manhattan!  559.0 Entire home/apt                                         No pets             2.0                  4                 2.0 Dallas
                             Sunny Brooklyn room  227.0    Private room                                         No pets             7.0                  2                 3.0 Dallas
                 Charming Suite in Historic Home  348.0 Entire home/apt               No parties & No children under 10             1.0                  3                 3.0 Dallas
              2 Bedroom Apt in downtown Brooklyn 1180.0 Entire home/apt No visitors & No children under 10 & No parties             4.0                  5                 2.0 Dallas
              Quite & Cozy High Raise Atmosphere  635.0    Private room                                      No smoking             1.0                  1                 5.0 Dallas
                          Upper east side duplex  819.0 Entire home/apt                                         No pets             3.0                  7                 2.0 Dallas
                Central Park west. Big Cozy Room  709.0    Private room                                         No pets             1.0                  2                 4.0 Dallas
            Huge Private Room Near Prospect Park   73.0    Private room                            No parties & No pets             7.0                  2                 2.0 Dallas
 Private room close to the center of Williamburg  231.0    Private room              No visitors & No children under 10             1.0                  1                 2.0 Dallas
                         Spacious cozy apartment  314.0 Entire home/apt                            No children under 10             2.0                  3                 1.0 Dallas
Charming Garden Apartment in Brooklyn Brownstone  434.0 Entire home/apt                                     No visitors             2.0                  2                 3.0 Dallas
                                  Friendly hosts  806.0    Private room                                      No smoking             1.0                  2                 4.0 Dallas
        Minutes from JFK airport and famous mall  711.0    Private room                        No visitors & No parties             2.0                  2                 3.0 Dallas
Attractions in El Paso
                                                          Name  Latitude   Longitude                                                    Address          Phone                                                                                 Website    City
                             El Paso Zoo and Botanical Gardens 31.767612 -106.445150                  4001 E Paisano Dr, El Paso, TX 79905, USA (915) 212-0966                                                               http://www.elpasozoo.org/ El Paso
                                         El Paso Museum of Art 31.758588 -106.490269              1 Arts Festival Plaza, El Paso, TX 79901, USA (915) 212-0300                                                                       https://epma.art/ El Paso
                                 National Border Patrol Museum 31.903070 -106.448636 4315 Woodrow Bean Transmountain Dr, El Paso, TX 79924, USA (915) 759-6060                                                      http://www.borderpatrolmuseum.com/ El Paso
                                             San Jacinto Plaza 31.759619 -106.488523                    114 W Mills Ave, El Paso, TX 79901, USA (915) 534-0600                  https://new.elpasotexas.gov/parks-and-recreation/aquatics/spray-parks/ El Paso
                                                Casa de Azucar 31.833396 -106.440455                   4301 Leavell Ave, El Paso, TX 79904, USA        Unknown                                      https://www.atlasobscura.com/places/casa-de-azucar El Paso
                       El Paso Holocaust Museum & Study Center 31.762324 -106.491945                    715 N Oregon St, El Paso, TX 79902, USA (915) 351-0048                                                   http://www.elpasoholocaustmuseum.org/ El Paso
                                 Franklin Mountains State Park 31.911703 -106.517367            Tom Mays Park Access Rd, El Paso, TX 79911, USA (915) 444-9100 http://www.tpwd.state.tx.us/state-parks/parks/find-a-park/franklin-mountains-state-park El Paso
                        Old Fort Bliss Replica Cultural Center 31.800049 -106.426695                   5054 Pershing Rd, El Paso, TX 79925, USA (915) 588-8482               https://bliss.armymwr.com/programs/old-fort-bliss-replica-cultural-center El Paso
                                 El Paso Museum of Archaeology 31.903670 -106.449051 4301 Woodrow Bean Transmountain Dr, El Paso, TX 79924, USA (915) 755-4332                                                                     http://epmarch.org/ El Paso
                                                 Wigwam Museum 31.757817 -106.488339              110 E San Antonio Ave, El Paso, TX 79901, USA (915) 274-9531                                                               http://www.ghosts915.org/ El Paso
                                            Tom Lea Upper Park 31.774927 -106.491300                         900 Rim Rd, El Paso, TX 79902, USA (915) 212-0092                                        https://www.elpasotexas.gov/parks-and-recreation El Paso
                             Magoffin Home State Historic Site 31.762487 -106.476980                  1120 Magoffin Ave, El Paso, TX 79901, USA (915) 533-5147                                                       http://www.visitmagoffinhome.com/ El Paso
                                                House Of Sugar 31.833410 -106.440459                   4301 Leavell Ave, El Paso, TX 79904, USA        Unknown                                                                                 Unknown El Paso
                                                 Ascarate Park 31.752285 -106.402331                      6900 Delta Dr, El Paso, TX 79905, USA (915) 771-2380                                                    https://www.epcountyparks.com/parks/ El Paso
                                              Downtown El Paso 31.758954 -106.488691                    201 N Oregon St, El Paso, TX 79901, USA (915) 400-2294                                                             https://downtownelpaso.com/ El Paso
Keystone Heritage Park and the El Paso Desert Botanical Garden 31.820571 -106.563529                   4200 Doniphan Dr, El Paso, TX 79922, USA (915) 490-8571                                                    http://www.keystoneheritagepark.com/ El Paso
                                         Murchison Rogers Park 31.782629 -106.479791                     1600 Scenic Dr, El Paso, TX 79902, USA (915) 803-8914                                        https://www.elpasotexas.gov/parks-and-recreation El Paso
                                               Rio Bosque Park 31.640965 -106.310328                   10716 Socorro Rd, El Paso, TX 79927, USA (915) 747-8663                               https://www.utep.edu/cerm/rio-bosque/rio-bosque-home.html El Paso
               Centennial Museum and Chihuahuan Desert Gardens 31.769288 -106.505954               500 W University Ave, El Paso, TX 79968, USA (915) 747-5565                                                                 http://museum.utep.edu/ El Paso
                                    Chamizal National Memorial 31.767241 -106.454337               800 S San Marcial St, El Paso, TX 79905, USA (915) 532-7273                                                      https://www.nps.gov/cham/index.htm El Paso
Restaurants in El Paso
                                          Name  Average Cost                                                   Cuisines  Aggregate Rating    City
                                    Los Beto"s            34                               Tea, Chinese, Cafe, Desserts               4.4 El Paso
                Cev韄che Tapas Bar & Restaurant            35                                               BBQ, Seafood               4.4 El Paso
                    The Garden Cafe - The Fern            72                        Desserts, Pizza, Italian, BBQ, Cafe               4.1 El Paso
                                        Onesta            71                         BBQ, American, Desserts, Fast Food               4.3 El Paso
Downtown Kitchen & Bar - Courtyard by Marriott            87        Desserts, Pizza, Mexican, Bakery, Fast Food, Indian               3.2 El Paso
                                  Knight Rider            99                          Seafood, Mediterranean, Fast Food               3.1 El Paso
                            Panther Restaurant            48                                     Chinese, BBQ, Desserts               0.0 El Paso
                         The League Restaurant            55                                                Bakery, BBQ               3.1 El Paso
                                     West愆ross            25                   Pizza, Bakery, Fast Food, Cafe, American               3.5 El Paso
                                       Begonia            98                         Cafe, American, Mediterranean, BBQ               3.0 El Paso
                              Raju Chat Palace            34                  Desserts, Tea, Bakery, Fast Food, Chinese               3.9 El Paso
                   Coffee Shop - Centaur Hotel            73                               Tea, Cafe, American, Italian               0.0 El Paso
                               Soni Bhojnalaya            61                         Cafe, Pizza, Indian, Mediterranean               3.0 El Paso
                                       Concept            93                                    Bakery, Pizza, Desserts               3.9 El Paso
                         Wagh Bakri Tea Lounge            85                                  Cafe, Mexican, Pizza, BBQ               3.7 El Paso
                                      Shi Cafe            22              Desserts, Bakery, Fast Food, Chinese, Seafood               0.0 El Paso
                            The Celiac Kitchen            22                      Desserts, Tea, French, BBQ, Fast Food               0.0 El Paso
                                   Garden Chef            46                 Desserts, Mexican, Fast Food, Cafe, Indian               3.0 El Paso
                                    Veg Gulati            63                                   Fast Food, Cafe, Seafood               3.8 El Paso
                           Arora"s Veg. Corner            64 Desserts, Pizza, Italian, Bakery, Fast Food, Mediterranean               3.4 El Paso
                                           SFC            23                           BBQ, Indian, Desserts, Fast Food               2.8 El Paso
                                     Apna Swad            63                            Cafe, Bakery, Desserts, Seafood               2.9 El Paso
                                  Captain Grub            92                               Tea, French, Cafe, Fast Food               3.8 El Paso
                                 Pind Balluchi            51                             French, Bakery, BBQ, Fast Food               2.6 El Paso
                               Super Cake Shop            49                Tea, Mexican, BBQ, Fast Food, Mediterranean               2.8 El Paso
                                     Wow! Momo            78                 Desserts, Pizza, Fast Food, Cafe, American               2.6 El Paso
                          The Big Buddha Grill            59                                          Tea, BBQ, Italian               0.0 El Paso
                              Food Destination            50                         Chinese, American, Cafe, Fast Food               3.0 El Paso
                             Pan Asian Noodles            94                                    Bakery, Indian, Seafood               0.0 El Paso
                                    The Plough           100                                 Tea, Cafe, Bakery, Seafood               4.2 El Paso
Accommodations in El Paso
                                              NAME  price       room type                                    house_rules  minimum nights  maximum occupancy  review rate number    city
 Upper West / Morningside Heights Apt, Near Subway  290.0 Entire home/apt                                     No smoking             3.0                  2                 3.0 El Paso
                                    Midtown Studio  625.0 Entire home/apt                                     No smoking             3.0                  3                 2.0 El Paso
          Bedroom in Large Artist Loft in Brooklyn 1004.0    Private room                           No pets & No smoking             5.0                  2                 4.0 El Paso
                        Amazing Private Room in BK  848.0    Private room              No smoking & No children under 10             2.0                  2                 5.0 El Paso
                2 room, lower level home in Queens  735.0    Private room             No children under 10 & No visitors             2.0                  2                 4.0 El Paso
      Clean, Cozy, and Spacious Brooklyn Row House  107.0    Private room                                        No pets             2.0                  1                 4.0 El Paso
     Private Room 2 in East Village (Large Window) 1086.0    Private room                                    No visitors             1.0                  2                 5.0 El Paso
                   Chic Designer Home Guest Studio   61.0 Entire home/apt                       No visitors & No parties             2.0                  3                 2.0 El Paso
               Furnished room for rent - Manhattan  237.0    Private room                                     No smoking             3.0                  1                 3.0 El Paso
                                 423 ocean parkway  557.0    Private room No parties & No children under 10 & No smoking             1.0                  1                 2.0 El Paso
                    Magic Waters - Brooklyn Refuge  363.0 Entire home/apt                                     No parties             2.0                  2                 2.0 El Paso
                1 BR in 2 BR Apt (Upper East Side)  255.0    Private room                          No visitors & No pets             1.0                  2                 5.0 El Paso
                           Cozy East Village Loft!  896.0    Private room                 No children under 10 & No pets             3.0                  1                 5.0 El Paso
Renovated Apartment in Brooklyn - Steps to G Train 1089.0 Entire home/apt                                        No pets             6.0                  2                 4.0 El Paso
"""

# Split the string on new lines to get rows
rows = input_string.split('\n')

# Split each row based on whitespace to get individual elements
data = [re.split(r'\s{3,}', row) for row in rows]

# Write the data to a CSV file
csv_file_path = 'content/dallas_attractions.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file created at {csv_file_path}")
