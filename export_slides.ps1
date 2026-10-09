$pptPath = "C:\Users\eshant\Desktop\happiness\Personal_Wellbeing_Research_Presentation.pptx"
$outputDir = "C:\Users\eshant\Desktop\happiness\slides_img"

if (!(Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

$ppt = New-Object -ComObject PowerPoint.Application
$pres = $ppt.Presentations.Open($pptPath, [Microsoft.Office.Core.MsoTriState]::msoTrue, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse)

$slideIndex = 1
foreach ($slide in $pres.Slides) {
    $slideFile = Join-Path $outputDir ("slide_{0:D2}.png" -f $slideIndex)
    $slide.Export($slideFile, "PNG", 1920, 1080)
    $slideIndex++
}

$pres.Close()
$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()

Write-Output "Successfully exported $slideIndex slides to $outputDir"
