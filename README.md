spatula
=======

This Ansible role applies security best practice templates to Palo Alto Networks devices.

Purpose
=======

This role leverages the [Iron Skillet](https://iron-skillet.readthedocs.io/en/panos_v8.1/index.html) best practice templates to ensure that PAN-OS firewalls are configured in accordance with Palo Alto Networks [best practice recommendations](https://www.paloaltonetworks.com/documentation/best-practices).  These templates are downloaded from the following GitHub repo when the playbook is executed and applied to each device or to a Panorama management console.

- https://github.com/PaloAltoNetworks/iron-skillet

A [Best Practices Assessment](https://www.paloaltonetworks.com/services/bpa) may be run following the application of these templates in order to gauge the effectiveness of the resulting configuration.

Requirements
------------

This role utilizes the Python libraries listed below. All are available via [PyPI](https://pypi.org) and may be installed using the `pip` installer. The use of `virtualenv` is recommended in order to avoid system library conflicts.

* [pandevice](https://pypi.org/project/pandevice/) - Framework for interacting with Palo Alto Networks devices via API
* [pab-python](https://pypi.org/project/pan-python) - Multi-tool set for Palo Alto Networks PAN-OS, Panorama, WildFire and AutoFocus
* [xmltodict](https://pypi.org/project/XML2Dict/) - Convert between XML String and Python Dict

Role Variables
--------------

The variables used in this role are listed in the table below, along with default values (see defaults/main.yml).  Variables in __lowercase__ are playbook variables while __UPPERCASE__ variables are used for Jinja2 variable substitution in the configuration templates.  Some variables are marked as Panorama only while others are applicable to both Panorama and firewalls.

| Variable | Type | Default | Panorama | Panos | Description |
|:----------------------:|--------------------|:-----------------------:|:--------:|:-----:|:-----------------------------------------------------------------------:|
| device_type | panorama,panos | panorama | x | x | Panorama or firewall config |
| template_version | panos_v9.0,panos_v8.1,panos_v8.0 | panos_v9.0 | x | x | Template version |
| CONFIG_PANORAMA_IP | yes,no | yes | x |  | Panorama management interface config |
| PANORAMA_TYPE | static,cloud | static | x |  | Panorama management IP type |
| PANORAMA_NAME | string | panorama01 | x |  | Panorama hostname |
| PANORAMA_IP | string | 192.168.55.7 | x |  | Panorama IP |
| PANORAMA_MASK | string | 255.255.255.0 | x |  | Panorama netmask |
| PANORAMA_DG | string | 192.168.55.2 | x |  | Panorama default gateway |
| CONFIG_EXPORT_IP | string | 192.0.2.3 | x |  | IP address for scheduled config exports |
| STACK | string | sample_stack | x |  | Template stack for Panorama |
| DEVICE_GROUP | string | sample_devicegroup | x |  | Device-group name for Panorama |
| FW_NAME | string | panos-01 | x | x | Firewall hostname |
| MGMT_TYPE | dhcp-client,static | dhcp-client | x | x | Firewall management IP type |
| MGMT_IP | string | 192.0.2.6 | x | x | Firewall management IP |
| MGMT_MASK | string | 255.255.255.0 | x | x | Firewall management netmask |
| MGMT_DG | string | 192.0.2.7 | x | x | Firewall management default gateway |
| NTP_1 | string | 0.pool.ntp.org | x | x | Network Time Protocol Server |
| NTP_2 | string | 1.pool.ntp.org | x | x | Network Time Protocol Server 2 |
| ADMINISTRATOR_USERNAME | string | admin | x | x | Admin username |
| ADMINISTRATOR_PASSWORD | password | admin | x | x | Admin password |
| DNS_1 | string | 8.8.8.8 | x | x | Primary DNS server |
| DNS_2 | string | 8.8.4.4 | x | x | Secondary dns server |
| SINKHOLE_IPV4 | string | 72.5.65.111 | x | x | Sinkhole address IPv4 |
| SINKHOLE_IPV6 | string | 2600:5200::1 | x | x | Sinkhole address IPv6 |
| INTERNET_ZONE | string | untrust | x | x | Untrust zone to filter out in reports |
| EMAIL_PROFILE_GATEWAY | string | 192.0.2.1 | x | x | Email gateway address for critical alerts |
| EMAIL_PROFILE_FROM | string | sentfrom@yourdomain.com | x | x | From address in email alerts |
| EMAIL_PROFILE_TO | string | sendto@yourdomain.com | x | x | To address in email alerts |
| SYSLOG_SERVER | string | 192.0.2.2 | x | x | Syslog server IP address |
| API_KEY_LIFETIME | string | 525600 | x | x | Lifetime for the API key in minutes |
| INCLUDE_PAN_EDL | yes,no | yes | x | x | Include the predefined Palo Alto Networks external lists security rules |


Dependencies
------------

This role is dependent on the official Palo Alto Networks Ansible modules, which are contained in the following Galaxy role:

* [PaloAltoNetworks.paloaltonetworks](https://galaxy.ansible.com/paloaltonetworks/paloaltonetworks)

The Palo Alto Networks Ansible modules utilize a provider `dict` for passing inventory and authentication credentials.  This `dict` may be defined once in the playbook with values for the variables `ip_address`, `username`, and `password` passed in via any supported method.

```yaml
vars:
  credentials:
    ip_address: '{{ ip_address }}'
    username: '{{ username }}'
    password: '{{ password }}'
```

Example Playbooks
-----------------

The following are examples of Ansible playbooks that leverage this role to apply security best practice templates to Panorama and a firewall:

*Panorama:*
```yaml
---
- name: Stage Panorama with best practice templates for PAN-OS 9.0
  hosts: all
  connection: local
  gather_facts: False

  vars:
    credentials:
      ip_address: '{{ ip_address }}'
      username: '{{ username }}'
      password: '{{ password }}'
    device_type: 'panorama'
    template_version: 'panos_v9.0'
  vars_files:
    - panorama_vars.yml
      
  roles:
    - role: stealthllama.spatula
```

*Firewall:*
```yaml
---
- name: Stage firewall with best practice templates for PAN-OS 8.1
  hosts: all
  connection: local
  gather_facts: False

  vars:
    credentials:
      ip_address: '{{ ip_address }}'
      username: '{{ admin }}'
      password: '{{ password }}'
    device_type: 'panos'
    template_version: 'panos_v8.1'
  vars_files:
    - fw_vars.yml
      
  roles:
    - role: stealthllama.spatula
```

License
-------
Apache 2.0

Author Information
------------------
Role created by Robert Hagen ([@stealthllama](https://github.com/stealthllama)).
