
#Author Gustav0

#Convert to solid weapon format weighted weapons, still in testing stage.
#Version: 1.4
#Fixed Haran and Toukabou



import struct
import os
import shutil 
import tkinter as tk
from tkinter import messagebox

data_weighted = {
    "Weapons": {
        "Swords": {
            "4 Star": {
                "AmenomaKageuchi": {
                    "draw_vb": "7ab4088d",
                    "position_vb": "5e0231af",
                    "blend_vb": "c40b8ac0",
                    "texcoord_vb": "528f299f",
                    "ib": "0c247424"
                },
                "BlackcliffLongsword": {
                    "draw_vb": "361fdde0",
                    "position_vb": "18802bf2",
                    "blend_vb": "dd3d91ea",
                    "texcoord_vb": "cbccbec2",
                    "ib": "0cc8180c"
                },
                "PrototypeRancour": {
                    "draw_vb": "361fdde0",
                    "position_vb": "18802bf2",
                    "blend_vb": "dd3d91ea",
                    "texcoord_vb": "cbccbec2",
                    "ib": "0cc8180c"
                },
                "Toukabou": {
                    "draw_vb": "b45451b0",
                    "position_vb": "4449dcf9",
                    "blend_vb": "f2b0ebe0",
                    "texcoord_vb": "e9e099b7",
                    "ib": "097866ce"
                }
            },
            "5 Star": {
                "HaranGeppaku": {
                    "draw_vb": "6c96b19c",
                    "position_vb": "a07c44cc",
                    "blend_vb": "c148d5d2",
                    "texcoord_vb": "2dda1417",
                    "ib": "06862c93"
                }
            }
        },
        "Polearms": {
            "4 Star": {
                "BlackcliffPole": {
                    "draw_vb": "0c7e3438",
                    "position_vb": "3c37e40c",
                    "blend_vb": "0c7e3438",
                    "texcoord_vb": "f89169d4",
                    "ib": "b6d2b63b"
                },
                "PrototypeStarglitter": {
                    "draw_vb": "7d43358a",
                    "position_vb": "3c37e40c",
                    "blend_vb": "0c7e3438",
                    "texcoord_vb": "f89169d4",
                    "ib": "b6d2b63b"
                }
            }
        }
    }
}
data = {
  "Weapons": {
    "Swords": {
      "4 Star": {
        "AlleyFlash": {
          "draw_vb": "2a527815",
          "ib": "0e69854d"
        },
        "BrokenIsshinBlade": {
          "draw_vb": "0a6a7c16",
          "ib": "740b7b00"
        },
        "CinnabarSpindle": {
          "draw_vb": "b9a33aba",
          "ib": "1fed9b21"
        },
        "DockhandsAssistant": {
          "draw_vb": "2cbb1d41",
          "ib": "f849c6a9"
        },
        "FavoniusSword": {
          "draw_vb": "5abde609",
          "ib": "0e69854d"
        },
        "FesteringDesire": {
          "draw_vb": "5107fe33",
          "ib": "caa58be1"
        },
        "FinaleoftheDeep": {
          "draw_vb": "99d58fb3",
          "ib": "f05a1673"
        },
        "FleuveCendreFerryman": {
          "draw_vb": "260f862d",
          "ib": "32da858d"
        },
        "Flute": {
          "draw_vb": "feda7529",
          "ib": "d7fb87ab"
        },
        "IronSting": {
          "draw_vb": "6d03a324",
          "ib": "c3442691"
        },
        "KagotsurubeIsshin": {
          "draw_vb": "0a6a7c16",
          "ib": "740b7b00"
        },
        "LionsRoar": {
          "draw_vb": "eca7244d",
          "ib": "fad3a13e"
        },
        "PrizedIsshinBlade": {
          "draw_vb": "0a6a7c16",
          "ib": "740b7b00"
        },
        "RoyalLongsword": {
          "draw_vb": "537c678b",
          "ib": "20f011e5"
        },
        "SacrificialSword": {
          "draw_vb": "537c678b",
          "ib": "20f011e5"
        },
        "SapwoodBlade": {
          "draw_vb": "67b13076",
          "ib": "4a0e68c8"
        },
        "SwordOfDescension": {
          "draw_vb": "6c5aef41",
          "ib": "4a74ca33"
        },
        "SwordOfNarzissenkreuzOusia": {
          "draw_vb": "d52859fe",
          "ib": "3770e77b"
        },
        "SwordOfNarzissenkreuzPneuma": {
          "draw_vb": "d52859fe",
          "ib": "3770e77b"
        },
        "WolfFang": {
          "draw_vb": "77533699",
          "ib": "3da78ab4"
        },
        "XiphosMoonlight": {
          "draw_vb": "f23efcd1",
          "ib": "98fa1ef4"
        }
      },
      "5 Star": {
        "Absolution": {
          "draw_vb": "42675343",
          "ib": "1d34541d"
        },
        "AquilaFavonia": {
          "draw_vb": "258b61e8",
          "ib": "4c6270ce"
        },
        "FreedomSworn": {
          "draw_vb": "97979da2",
          "ib": "33c15eef"
        },
        "JadeCutter": {
          "draw_vb": "557101f5",
          "ib": "4853de0b"
        },
        "KeyOfKhajNisut": {
          "draw_vb": "49d0fdd7",
          "ib": "e27ca3cd"
        },
        "LightOfFoliarIncision": {
          "draw_vb": "bf7ba8b7",
          "ib": "dd3e78ac"
        },
        "Mistsplitter": {
          "draw_vb": "dda585aa",
          "ib": "914f8315"
        }
      }
    },
    "Claymores": {
      "4 Star": {
        "Akuoumaru": {
          "draw_vb": "28482c4d",
          "ib": "7a5888ca"
        },
        "Bell": {
          "draw_vb": "8e05cc48",
          "ib": "75eaaea1"
        },
        "FavoniusGreatsword": {
          "draw_vb": "945cd6d3",
          "ib": "21176dc0"
        },
        "ForestRegalia": {
          "draw_vb": "200cead2",
          "ib": "7edf08da"
        },
        "LithicBlade": {
          "draw_vb": "02ff1fb1",
          "ib": "1e471ae7"
        },
        "MailedFlower": {
          "draw_vb": "94b08c60",
          "ib": "db2f1b0d"
        },
        "MakhairaAquamarine": {
          "draw_vb": "c82db298",
          "ib": "b793be3a"
        },
        "Rainslasher": {
          "draw_vb": "02ff1fb1",
          "ib": "1e471ae7"
        },
        "RoyalGreatsword": {
          "draw_vb": "76235162",
          "ib": "3ab6c5d7"
        },
        "SacrificialGreatsword": {
          "draw_vb": "76235162",
          "ib": "3ab6c5d7"
        },
        "SeaLord": {
          "draw_vb": "9aaeba7f",
          "ib": "c8287f96"
        },
        "SerpentSpine": {
          "draw_vb": "1e84b863",
          "ib": "b140d661"
        },
        "SnowTombed": {
          "draw_vb": "943dee5d",
          "ib": "939e75f5"
        },
        "Whiteblind": {
          "draw_vb": "22802011",
          "ib": "4fc6fa1f"
        }
      },
      "5 Star": {
        "BeaconOfTheReedSea": {
          "draw_vb": "6c3dc4a7",
          "ib": "b6041a0b"
        },
        "Redhorn": {
          "draw_vb": "17e64426",
          "ib": "e4011c08"
        },
        "SkywardPride": {
          "draw_vb": "c1430748",
          "ib": "75f971c6"
        },
        "SongOfBrokenPines": {
          "draw_vb": "7ebe84c4",
          "ib": "ae2bfaff"
        },
        "Unforged": {
          "draw_vb": "7e391a0c",
          "ib": "af679171"
        },
        "Verdict": {
          "draw_vb": "ddf822c4",
          "ib": "360f93cd"
        },
        "WolfsGravestone": {
          "draw_vb": "7f4c0368",
          "ib": "389602b9"
        }
      }
    },
    "Polearms": {
      "4 Star": {
        "VortexVanquisher": {
          "draw_vb": "107565f1",
          "ib": "0804ee80"
        },
        "CrescentPike": {
          "draw_vb": "0c7a979d",
          "ib": "6a774547"
        },
        "Deathmatch": {
          "draw_vb": "86df9fed",
          "ib": "23953878"
        },
        "DragonsBane": {
          "draw_vb": "5d5710d0",
          "ib": "cc59be65"
        },
        "DragonspineSpear": {
          "draw_vb": "05549719",
          "ib": "e67288a0"
        },
        "FavoniusLance": {
          "draw_vb": "cb54f1f4",
          "ib": "1cfef8f9"
        },
        "Kitain": {
          "draw_vb": "214eb2c0",
          "ib": "3ba4e2b4"
        },
        "LithicSpear": {
          "draw_vb": "5d5710d0",
          "ib": "cc59be65"
        },
        "MissiveWindspear": {
          "draw_vb": "1dd762c4",
          "ib": "273e3a3b"
        },
        "Moonpiercer": {
          "draw_vb": "8a4b06af",
          "ib": "535eb1ad"
        },
        "TheCatch": {
          "draw_vb": "98017505",
          "ib": "8d293d55"
        },
        "WavebreakersFin": {
          "draw_vb": "bd894607",
          "ib": "94c680c0"
        }
      },
      "5 Star": {
        "CalamityQueller": {
          "draw_vb": "1261ca87",
          "ib": "5bf44f5e"
        },
        "EngulfingLightning": {
          "draw_vb": "297be42e",
          "ib": "e1ba0ff2"
        },
        "JadeWingedSpear": {
          "draw_vb": "62f85774",
          "ib": "2979ad00"
        },
        "SkywardSpine": {
          "draw_vb": "83498c52",
          "ib": "0a419395"
        },
        "StaffOfHoma": {
          "draw_vb": "4cc8add8",
          "ib": "412330a9"
        },
        "StaffOfTheScarletSands": {
          "draw_vb": "c3b21723",
          "ib": "b9138fed"
        }
      }
    }
  }
}

def clamp(value, min_value=0.0, max_value=1.0):
    return max(min_value, min(value, max_value))

def find_buf_files(prefix):
    position_file = None
    texcoord_file = None
    for file in os.listdir('.'):
        if file.lower().endswith('position.buf'):
            position_file = file
        elif file.lower().endswith('texcoord.buf'):
            texcoord_file = file
    return position_file, texcoord_file

def create_weapon_folder(weapon_name):
    folder_name = f"{weapon_name}_mod"
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

def generate_ini(weapon_name, weapon_data, folder_name, weighted=False):
    if weighted:
        ini_content = f"""; Overrides -------------------------

[TextureOverride{weapon_name}Position]
hash = {weapon_data['position_vb']}
vb0 = Resource{weapon_name}Position

[TextureOverride{weapon_name}Blend]
hash = {weapon_data['blend_vb']}
vb1 = Resource{weapon_name}Blend
handling = skip
draw = 5500,0 

[TextureOverride{weapon_name}Texcoord]
hash = {weapon_data['texcoord_vb']}
vb1 = Resource{weapon_name}Texcoord

[TextureOverride{weapon_name}VertexLimitRaise]
hash = {weapon_data['draw_vb']}

[TextureOverride{weapon_name}IB]
hash = {weapon_data['ib']}
handling = skip
drawindexed = auto

[TextureOverride{weapon_name}Head]
hash = {weapon_data['ib']}
match_first_index = 0
ib = Resource{weapon_name}HeadIB
ps-t0 = Resource{weapon_name}HeadDiffuse
ps-t1 = Resource{weapon_name}HeadLightMap

; Resources -------------------------

[Resource{weapon_name}Position]
type = Buffer
stride = 40
filename = {weapon_name}Position.buf

[Resource{weapon_name}Blend]
type = Buffer
stride = 32
filename = {weapon_name}Blend.buf

[Resource{weapon_name}Texcoord]
type = Buffer
stride = 20
filename = {weapon_name}Texcoord.buf

[Resource{weapon_name}HeadIB]
type = Buffer
format = DXGI_FORMAT_R32_UINT
filename = {weapon_name}Head.ib

[Resource{weapon_name}HeadDiffuse]
filename = {weapon_name}HeadDiffuse.dds

[Resource{weapon_name}HeadLightMap]
filename = {weapon_name}HeadLightMap.dds

[Resource{weapon_name}HeadMetalMap]
filename = {weapon_name}HeadMetalMap.dds

[Resource{weapon_name}HeadDiffuseGuide]
filename = {weapon_name}HeadDiffuseGuide.dds
"""
    else:
        ini_content = f"""[TextureOverride{weapon_name}]
hash = {weapon_data['draw_vb']}
vb0 = Resource{weapon_name}

[TextureOverride{weapon_name}IB]
hash = {weapon_data['ib']}
handling = skip
drawindexed = auto

[TextureOverride{weapon_name}Head]
hash = {weapon_data['ib']}
match_first_index = 0
ib = Resource{weapon_name}HeadIB
ps-t0 = Resource{weapon_name}HeadDiffuse
ps-t1 = Resource{weapon_name}HeadLightMap

; Resources -------------------------

[Resource{weapon_name}]
type = Buffer
stride = 28
filename = {weapon_name}Position.buf

[Resource{weapon_name}HeadIB]
type = Buffer
format = DXGI_FORMAT_R32_UINT
filename = {weapon_name}Head.ib

[Resource{weapon_name}HeadDiffuse]
filename = {weapon_name}HeadDiffuse.dds

[Resource{weapon_name}HeadLightMap]
filename = {weapon_name}HeadLightMap.dds
"""
    return ini_content

def convert_and_split(weapon_name, folder_name):
    input_buf_files = [file for file in os.listdir('.') if file.lower().endswith('.buf')]
    
    if len(input_buf_files) == 0:
        print(f"Error: Could not find any .buf files in the current directory.")
        return
    elif len(input_buf_files) > 1:
        print(f"Error: Found multiple .buf files in the current directory. Please ensure only one .buf file is present.")
        return
    
    input_buf_path = input_buf_files[0]
    
    if not input_buf_path:
        print(f"Error: Could not find a Position.buf file in the current directory.")
        return

    output_position_path = os.path.join(folder_name, f'{weapon_name}Position.buf')
    output_texcoord_path = os.path.join(folder_name, f'{weapon_name}Texcoord.buf')
    output_blend_path = os.path.join(folder_name, f'{weapon_name}Blend.buf')

    position_data = bytearray()
    texcoord_data = bytearray()
    blend_data = bytearray()
    
    input_stride = 28
    position_stride = 40
    texcoord_stride = 20
    blend_stride = 32

    with open(input_buf_path, 'rb') as input_file:
        input_data = input_file.read()
    
    input_data_length = len(input_data)
    vertex_count = input_data_length // input_stride
    
    print(f"Input file size: {input_data_length} bytes")
    print(f"Input stride: {input_stride} bytes")
    print(f"Vertex count: {vertex_count}")


    for i in range(vertex_count):
        offset = i * input_stride

        position = struct.unpack_from('<4e', input_data, offset)
        normal = struct.unpack_from('<4b', input_data, offset + 8)
        color = struct.unpack_from('<4B', input_data, offset + 12)
        texcoord0 = struct.unpack_from('<2e', input_data, offset + 16)
        texcoord1 = struct.unpack_from('<2e', input_data, offset + 20)
        tangent = struct.unpack_from('<4b', input_data, offset + 24)
        if weapon_name == "Toukabou":
            # Rotate -180° around Z axis
            x, y, z = position[:3]
            rotated_x = -x
            rotated_y = -y
            converted_position = struct.pack('<3f', rotated_x, rotated_y, z)
            
            # Rotate normal to match new position
            nx, ny, nz = (v / 127 for v in normal[:3])
            rotated_nx = -nx
            rotated_ny = -ny
            rotated_nz = -nz
            converted_normal = struct.pack('<3f', rotated_nx, rotated_ny, rotated_nz)
            
            # Rotate tangent to match new position
            tx, ty, tz, tw = (v / 255 for v in tangent)
            rotated_tx = -tx
            rotated_ty = -ty
            converted_tangent = struct.pack('<4f', rotated_tx, rotated_ty, tz, tw)
        else:
            converted_position = struct.pack('<3f', *position[:3])
            converted_normal = struct.pack('<3f', *(v / 127 for v in normal[:3]))
            converted_tangent = struct.pack('<4f', *(v / 255 for v in tangent))

        position_data.extend(converted_position)
        position_data.extend(converted_normal)
        position_data.extend(converted_tangent)

        converted_color = struct.pack('<4B', *color)
        converted_texcoord0 = struct.pack('<2f', *texcoord0)
        converted_texcoord1 = struct.pack('<2f', *texcoord1)

        texcoord_data.extend(converted_color)
        texcoord_data.extend(converted_texcoord0)
        texcoord_data.extend(converted_texcoord1)

    blend_weights = struct.pack('<4f', 1.0, 0.0, 0.0, 0.0)
    
    if weapon_name in ["Toukabou", "HaranGeppaku", "BlackcliffPole", "PrototypeStarglitter"]:
        blend_indices = struct.pack('<4I', 0, 1, 0, 0)
    else:
        blend_indices = struct.pack('<4I', 1, 0, 0, 0)

    for _ in range(vertex_count + 1):
        blend_data.extend(blend_weights)
        blend_data.extend(blend_indices)

    with open(output_position_path, 'wb') as output_file:
        output_file.write(position_data)

    with open(output_texcoord_path, 'wb') as output_file:
        output_file.write(texcoord_data)

    with open(output_blend_path, 'wb') as output_file:
        output_file.write(blend_data)

    print(f"Position output file size: {len(position_data)} bytes")
    print(f"Position output stride: {position_stride} bytes")
    print(f"Texcoord output file size: {len(texcoord_data)} bytes")
    print(f"Texcoord output stride: {texcoord_stride} bytes")
    print(f"Blend output file size: {len(blend_data)} bytes")
    print(f"Blend output stride: {blend_stride} bytes")
    print(f"Output vertex count: {vertex_count}")
    print(f"Blend buffer vertex count: {vertex_count + 1}")

def convert_and_merge(weapon_name, folder_name):
    position_buf_path, texcoord_buf_path = find_buf_files('')
    if not position_buf_path or not texcoord_buf_path:
        print(f"Error: Could not find Position.buf and Texcoord.buf files for {weapon_name}.")
        return

    output_buf_path = os.path.join(folder_name, f'{weapon_name}Position.buf')
    converted_data = bytearray()
    
    with open(position_buf_path, 'rb') as position_file:
        position_data = position_file.read()
        
    position_stride = 40
    position_data_length = len(position_data)
    vertex_count = position_data_length // position_stride
    
    print(f"Position.buf size: {position_data_length} bytes")
    print(f"Position stride: {position_stride} bytes")
    print(f"Vertex count: {vertex_count}")

    with open(texcoord_buf_path, 'rb') as texcoord_file:
        texcoord_data = texcoord_file.read()
        
    texcoord_stride = 20
    texcoord_data_length = len(texcoord_data)
    
    print(f"Texcoord.buf size: {texcoord_data_length} bytes")
    print(f"Texcoord stride: {texcoord_stride} bytes")

    for i in range(vertex_count):
        position_offset = i * position_stride
        texcoord_offset = i * texcoord_stride

        position = struct.unpack_from('<3f', position_data, position_offset)
        normal = struct.unpack_from('<3f', position_data, position_offset + 12)
        tangent = struct.unpack_from('<4f', position_data, position_offset + 24)

        color = struct.unpack_from('<4B', texcoord_data, texcoord_offset)
        texcoord0 = struct.unpack_from('<2f', texcoord_data, texcoord_offset + 4)
        texcoord1 = struct.unpack_from('<2f', texcoord_data, texcoord_offset + 12)

        converted_position = struct.pack('<4e', *position, 1.0)
        converted_normal = struct.pack('<4b', 
            *[int(clamp(v * 127, -127, 127)) for v in normal],
            0
        )
        converted_color = struct.pack('<4B', *color)
        converted_texcoord0 = struct.pack('<2e', *texcoord0)
        converted_texcoord1 = struct.pack('<2e', *texcoord1)
        
        converted_tangent = struct.pack('<4B', 
            *[int(clamp(v * 255, 0, 255)) for v in tangent[:3]],
            int(clamp(tangent[3] * 255, 0, 255))
        )
        
        converted_data.extend(converted_position)
        converted_data.extend(converted_normal)
        converted_data.extend(converted_color)
        converted_data.extend(converted_texcoord0)
        converted_data.extend(converted_texcoord1)
        converted_data.extend(converted_tangent)

    with open(output_buf_path, 'wb') as output_file:
        output_file.write(converted_data)

    print(f"Merged output file size: {len(converted_data)} bytes")
    print(f"Merged output stride: 28 bytes")
    print(f"Output vertex count: {vertex_count}")

def main():
    class WeaponConverterApp:
        def __init__(self, master):
            self.master = master
            master.title("Weapon Converter")
            master.geometry("400x300")  

          
            self.frame = tk.Frame(master, padx=20, pady=20)
            self.frame.pack(fill=tk.BOTH, expand=True)

            self.label = tk.Label(self.frame, text="Select Weapon Type:", font=("Times New Roman", 12))
            self.label.grid(row=0, column=0, sticky="w", pady=(0, 5))

            self.weapon_type_var = tk.StringVar()
            
            weapon_types = list(set(list(data_weighted['Weapons'].keys()) + list(data['Weapons'].keys())))
            self.weapon_type_menu = tk.OptionMenu(self.frame, self.weapon_type_var, 
                *weapon_types, command=self.update_rarities)
            self.weapon_type_menu.grid(row=0, column=1, sticky="ew", pady=(0, 5))

            self.label_rarity = tk.Label(self.frame, text="Select Rarity:", font=("Times New Roman", 12))
            self.label_rarity.grid(row=1, column=0, sticky="w", pady=(0, 5))

            self.rarity_var = tk.StringVar()
            self.rarity_menu = tk.OptionMenu(self.frame, self.rarity_var, "")
            self.rarity_menu.grid(row=1, column=1, sticky="ew", pady=(0, 5))

            self.label_weapon = tk.Label(self.frame, text="Select Weapon:", font=("Times New Roman", 12))
            self.label_weapon.grid(row=2, column=0, sticky="w", pady=(0, 5))

            self.weapon_var = tk.StringVar()
            self.weapon_menu = tk.OptionMenu(self.frame, self.weapon_var, "")
            self.weapon_menu.grid(row=2, column=1, sticky="ew", pady=(0, 5))

            self.weighted_var = tk.BooleanVar()
            self.weighted_checkbox = tk.Checkbutton(self.frame, text="Use Weighted Conversion", variable=self.weighted_var, command=self.update_weapons_list)
            self.weighted_checkbox.grid(row=3, column=0, columnspan=2, sticky="w", pady=(10, 5))
            
           
            self.tooltip = tk.Label(self.frame, text="For Solid > Animated(Weighted) weapon convert\ne.g., Mistsplitter to Amenoma", 
                                    font=("Times New Roman", 9), bg="lightyellow", relief="solid", borderwidth=1)
            self.tooltip.grid(row=4, column=0, columnspan=2, sticky="w", pady=(0, 5))
            self.tooltip.grid_remove()  
            
            self.weighted_checkbox.bind("<Enter>", self.show_tooltip)
            self.weighted_checkbox.bind("<Leave>", self.hide_tooltip)

            self.convert_button = tk.Button(self.frame, text="Convert", command=self.convert, bg="#4CAF50", fg="white", font=("Times New Roman", 12, "bold"))
            self.convert_button.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(20, 0))

            
            self.frame.columnconfigure(1, weight=1) 

    
            self.master.tk.call('tk', 'scaling', 1.0)
            self.master.option_add("*Font", "Times New Roman 9")

        def show_tooltip(self, event):
            self.tooltip.grid()

        def hide_tooltip(self, event):
            self.tooltip.grid_remove()

        def update_rarities(self, *args):
            weapon_type = self.weapon_type_var.get()
            rarities = set()
            if weapon_type in data_weighted['Weapons']:
                rarities.update(data_weighted['Weapons'][weapon_type].keys())
            if weapon_type in data['Weapons']:
                rarities.update(data['Weapons'][weapon_type].keys())
            rarities = sorted(list(rarities))
            self.rarity_var.set(rarities[0] if rarities else "")
            self.rarity_menu['menu'].delete(0, 'end')
            for rarity in rarities:
                self.rarity_menu['menu'].add_command(label=rarity, command=tk._setit(self.rarity_var, rarity, self.update_weapons))

            self.update_weapons()

        def update_weapons(self, *args):
            self.update_weapons_list()

        def update_weapons_list(self):
            weapon_type = self.weapon_type_var.get()
            rarity = self.rarity_var.get()
            weighted = self.weighted_var.get()
            
            weapons = set()
            if weighted and weapon_type in data_weighted['Weapons'] and rarity in data_weighted['Weapons'][weapon_type]:
                weapons.update(data_weighted['Weapons'][weapon_type][rarity].keys())
            if not weighted and weapon_type in data['Weapons'] and rarity in data['Weapons'][weapon_type]:
                weapons.update(data['Weapons'][weapon_type][rarity].keys())
            
            weapons = sorted(list(weapons))
            
            self.weapon_var.set(weapons[0] if weapons else "")
            self.weapon_menu['menu'].delete(0, 'end')
            for weapon in weapons:
                self.weapon_menu['menu'].add_command(label=weapon, command=tk._setit(self.weapon_var, weapon))

        def convert(self):
            weapon_type = self.weapon_type_var.get()
            rarity = self.rarity_var.get()
            weapon_name = self.weapon_var.get()
            weighted = self.weighted_var.get()

            if not weapon_type or not rarity or not weapon_name:
                messagebox.showerror("Error", "Please select all options.")
                return

            folder_name = create_weapon_folder(weapon_name)
            selected_data = data_weighted if weighted else data

            ini_content = generate_ini(weapon_name, selected_data['Weapons'][weapon_type][rarity][weapon_name], folder_name, weighted)
            ini_path = os.path.join(folder_name, f'{weapon_name}.ini')
            with open(ini_path, 'w') as f:
                f.write(ini_content)

            if weighted:
                convert_and_split(weapon_name, folder_name)
            else:
                convert_and_merge(weapon_name, folder_name)

      
            existing_files = [
                ('*Head.ib', f'{weapon_name}Head.ib'),
                ('*HeadDiffuse.dds', f'{weapon_name}HeadDiffuse.dds'),
                ('*HeadLightMap.dds', f'{weapon_name}HeadLightMap.dds')
            ]
            for source_pattern, target_name in existing_files:
                matching_files = [f for f in os.listdir('.') if f.endswith(source_pattern[1:])]
                if matching_files:
                    source_file = matching_files[0]
                    target_file = os.path.join(folder_name, target_name)
                    shutil.copy(source_file, target_file)
                    print(f"Copied and renamed {source_file} to {target_file}.")
                else:
                    print(f"Warning: No file matching {source_pattern} found. Please add {target_name} manually to {folder_name}.")

            messagebox.showinfo("Success", f"Files for {weapon_name} have been generated in {folder_name}.")
            print(f"All files for {weapon_name} have been generated, renamed, and organized in the {folder_name} folder.")

    root = tk.Tk()
    app = WeaponConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()