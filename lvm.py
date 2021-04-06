import os
os.system("tput setaf 3")
os.system("tput setab 8")

print("		<<<<<<Welcome To LVM Menu>>>>>>		")
print("*"*50)
ch="y"

print( """ 
press 1: To display all the available disks
press 2: To create PV(physical volume)
press 3: To display PV(physical volume)
press 4: To create VG(volume group)
press 5: To display VG(volume group)
press 6: To create LV(logical volume)
press 7: To display LV(logical volume)
press 8: To mount
press 9: To format the partition
press 10: To extend the size of LV
""")

while ch=='y':
	
	choice=int(input("Enter ur choice:"))
	if choice==1:
		os.system("lsblk")
	elif choice==2:
		try:
			pvname=input("Enter Phisical volume name:")
		except:
			print("Enter name properly!!")
		else:
			os.system(f"pvcreate /dev/{pvname}")
	
	elif choice==3:
		try:
			pvname=input("Enter Phisical volume name:")
		except:
			print("Enter name properly!!")
		else:
			os.system(f"pvdisplay /dev/{pvname}")
		
	elif choice==4:
		try:
			vgname=input("Enter volume group name:")
			pvname=input("Enter Phisical volume name:")
		except:
			print("Enter details properly!!")
		else:
			os.system(f"vgcreate {vgname} /dev/{pvname}")

	elif choice==5:
		try:
			vgname=input("Enter volume group name:")
		except:
			print("Enter details properly!!")
		else:
			os.system(f"vgdisplay {vgname}")
	elif choice==6:
		try:
			lvname=input("Enter lv name:")
			vgname=input("Enter volume group name:")
			size=int(input("Enter size of the volume:"))
		except:
			print("Enter details properly!!")
		else:
			os.system(f"lvcreate --size {size}G --name {lvname} {vgname}")
		
	elif choice==7:
		try:
			lvname=input("Enter lv name:")
			vgname=input("Enter volume group name:")
		except:
			print("Enter details properly!!")
		else:
			os.system(f"lvdisplay {vgname}/{lvname}")

	elif choice==8:
		try:
			lvname=input("Enter lv name:")
			vgname=input("Enter volume group name:")
			folder=input("Enter directory name to which u want to mount")
		except:
			print("Enter details properly!!")
		else:
			os.system(f"mount /dev/{vgname}/{lvname} /{folder}")

	elif choice==9:
		try:
			frmt=input("What do u want to format(enter full path):")
		except:
			print("enter proper name!!")
		else:
			os.system(f"mkfs.ext4 {frmt}")
	elif choice==10:
		try:
			lvname=input("Enter lv name:")
			vgname=input("Enter volume group name:")
			size=int(input("Enter size of the volume:"))
		except:
			print("Enter details properly!!")
		else:
			os.system(f"lvextend --size +{size}G /dev/{vgname}/{lvname}")
			os.system("resize2fs /{vgname}/{lvname}")
		
	else:
		print("INVALID CHIOCE!!!!")
	ch=input("do you want to continue:(y/n)")

