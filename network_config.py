from netmiko import connectHandler
router = {
	"device_type":"cisco_ios",
	"host":"sandbox-iosxe-latex-1.cisco.com",
	"username";"admin",
	"password":"C1sco12345",
	"port":22,
}
try:
connection = connectHandler(**router)
print
