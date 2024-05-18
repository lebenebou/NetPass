# NetPass
A simple python script which fetches saved network passwords on Windows

## Usage
### Example 1
`python netpass.py -name myNetwork`

Output:
```cmd
myNetwork|myPassword
```
### Example 2
`python netpass.py -all -json`

Output:
```json
{
    "epochTimestamp": 1716017139,
    "networks": [
        {
            "name": "myNetwork",
            "password": "myPassword"
        },
        {
            "name": "myNetwork2",
            "password": "mySecondPassword"
        }
    ]
}
```
### Example 3
`python netpass.py -all -csv`

Output:
```csv
myNetwork,myPassword
myNetwork2,mySecondPassword
```