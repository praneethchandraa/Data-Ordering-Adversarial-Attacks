### Results


<table>
  <tr>
   <td><strong>Dataset</strong>
   </td>
   <td><strong>Source</strong>
   </td>
   <td><strong>Surrogate</strong>
   </td>
   <td><strong>Attack Policy</strong>
   </td>
   <td><strong>Attack Type</strong>
   </td>
   <td><strong>Test Acc</strong>
   </td>
   <td><strong>Delta Acc</strong>
   </td>
  </tr>
  <tr>
   <td>CIFAR 10
   </td>
   <td>ResNet18
   </td>
   <td>LeNet5
   </td>
   <td>Batch Reordering
   </td>
   <td>Low - High
   </td>
   <td><strong>74% </strong>
   </td>
   <td><strong>-16.3%</strong>
   </td>
  </tr>
  <tr>
   <td>CIFAR 10
   </td>
   <td>ResNet18
   </td>
   <td>LeNet5
   </td>
   <td>Batch Reordering
   </td>
   <td>High - Low
   </td>
   <td><strong>78% </strong>
   </td>
   <td><strong>-12.3%</strong>
   </td>
  </tr>
  <tr>
   <td>CIFAR 10
   </td>
   <td>ResNet18
   </td>
   <td>LeNet5
   </td>
   <td>Batch Reordering
   </td>
   <td>Oscillation Inward
   </td>
   <td><strong>77%</strong>
   </td>
   <td><strong>-13.3%</strong>
   </td>
  </tr>
  <tr>
   <td>CIFAR 10
   </td>
   <td>ResNet18
   </td>
   <td>LeNet5
   </td>
   <td>Batch Reordering
   </td>
   <td>Oscillation outward
   </td>
   <td><strong>82%</strong>
   </td>
   <td><strong>-8.3%</strong>
   </td>
  </tr>
  <tr>
   <td>CIFAR 10
   </td>
   <td>ResNet18
   </td>
   <td>LeNet5
   </td>
   <td>Batch Reshuffling
   </td>
   <td>Low - High
   </td>
   <td><strong>37.2%</strong>
   </td>
   <td><strong>-62.1%</strong>
   </td>
  </tr>
  <tr>
   <td>CIFAR 10
   </td>
   <td>ResNet18
   </td>
   <td>LeNet5
   </td>
   <td>Batch Reshuffling
   </td>
   <td>High - Low
   </td>
   <td><strong>31.5%</strong>
   </td>
   <td><strong>-58.8%</strong>
   </td>
  </tr>
  <tr>
   <td>CIFAR 10
   </td>
   <td>ResNet18
   </td>
   <td>LeNet5
   </td>
   <td>Batch Reshuffling
   </td>
   <td>Oscillation Inward
   </td>
   <td><strong>28.2%</strong>
   </td>
   <td><strong>-62.1%</strong>
   </td>
  </tr>
  <tr>
   <td>CIFAR10
   </td>
   <td>ResNet18
   </td>
   <td>LeNet5
   </td>
   <td>Batch Reshuffling
   </td>
   <td>Oscillation outward
   </td>
   <td><strong>30.3%</strong>
   </td>
   <td><strong>-60.0%</strong>
   </td>
  </tr>
</table>



<table>
  <tr>
   <td><strong>Dataset</strong>
   </td>
   <td><strong>Source</strong>
   </td>
   <td><strong>Surrogate</strong>
   </td>
   <td><strong>Attack Policy</strong>
   </td>
   <td><strong>Attack Type</strong>
   </td>
   <td><strong>Test Acc</strong>
   </td>
  </tr>
  <tr>
   <td>SVHN
   </td>
   <td>VIT-b-16
   </td>
   <td>LeNet5
   </td>
   <td>
    Baseline- N/A
   </td>
   <td>-Baseline N/A
   </td>
   <td>82.76%
   </td>
  </tr>
</table>



<table>
  <tr>
   <td><strong>Dataset</strong>
   </td>
   <td><strong>Source</strong>
   </td>
   <td><strong>Surrogate</strong>
   </td>
   <td><strong>Attack Policy</strong>
   </td>
   <td><strong>Attack Type</strong>
   </td>
   <td><strong>Test Acc</strong>
   </td>
  </tr>
  <tr>
   <td>SVHN
   </td>
   <td>VIT-b-16
   </td>
   <td>LeNet5
   </td>
   <td>Batch Reordering
   </td>
   <td>Low - High
   </td>
   <td>76.1%
   </td>
  </tr>
  <tr>
   <td>SVHN
   </td>
   <td>VIT-b-16
   </td>
   <td>LeNet5
   </td>
   <td>Batch Reordering
   </td>
   <td>High - Low
   </td>
   <td>78.45%
   </td>
  </tr>
  <tr>
   <td>SVHN
   </td>
   <td>VIT-b-16
   </td>
   <td>LeNet5
   </td>
   <td>Batch Reordering
   </td>
   <td>Oscillations Inward
   </td>
   <td>54.8
   </td>
  </tr>
  <tr>
   <td>SVHN
   </td>
   <td>VIT-b-16
   </td>
   <td>LeNet5
   </td>
   <td>Batch Reordering
   </td>
   <td>Oscillations Outward
   </td>
   <td>54.6
   </td>
  </tr>
</table>

