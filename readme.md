# Service Account Manager with parameters

1. Use list of service account account and count it. 

## Commands 

```
# list all service accounts
arguments.py -l 

# add service Account from application 'Test' to project 'project1'
arguments.py -t 'test' -p 'project1' -a

# delete service account with id 0, project 'project1'
arguments.py -p 'project1' -i '0' -d # 

```

## Example

### Case #1

``` 
arguments.py -t 'test' -p 'project1' -a
arguments.py -t 'mercedes' -p 'project1' -a
arguments.py -t 'apple' -p 'project1' -a
arguments.py -l
```
#### Output 

```
service account id: 0, application: test, project project1
service account id: 1, application: mercedes, project project1
service account id: 2, application: apple, project project1
```

#### Delete object

```
arguments.py -i 1 -p 'project1' -d
arguments.py -l      
```
#### Output
```             
service account id: 0, application: test, project project1
service account id: 2, application: apple, project project1
```

#### Add

```
arguments.py -t 'apple' -p 'project1' -a
arguments.py -l 
```

#### Output 

```
service account id: 0, application: test, project project1
service account id: 2, application: apple, project project1
service account id: 1, application: apple, project project1
```