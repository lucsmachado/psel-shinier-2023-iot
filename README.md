# Processo Seletivo Shinier 2023
Desafio técnico do processo seletivo de 2023 para vaga de estágio em IoT na Shinier.
# Demonstração
![GIF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExanQ5bHEwcG00ZnN0ZWptZmdlbWZsd3MwNjYwdXlsaTVzNmpicHE3MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yaAJheSvcPorhZ4KJe/giphy.gif)
# Emulação da Raspberry Pi
Para configurar a máquina virtual usa-se o sotware livre e gratuito QEMU.

A seguir, seguem instruções para configuração do ambiente, considerando uma máquina HOST utilizando Debian/Ubuntu.

Primeiramente, instale o QEMU:
```bash
sudo apt-get install qemu-system
```

Faça o download de uma imagem do sistema operacional, Raspberry Pi OS a.k.a Raspbian. Nesse caso, optou-se por utilzar a versão Buster. O arquivo baixado está compactado, logo é preciso extraí-lo.
```bash
curl -O https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2021-05-28/2021-05-07-raspios-buster-armhf.zip
unzip -p 2021-05-07-raspios-buster-armhf.zip > raspbian.img
```

Siga [as instruções de mount da imagem](https://azeria-labs.com/emulate-raspberry-pi-with-qemu/).

Faça um clone do repositório [qemu-rpi-kernel](https://github.com/dhruvvyas90/qemu-rpi-kernel/tree/master) e copie os arquivos `kernel-qemu-5.4.51-buster` e `versatile-pb-buster.dtb` para seu diretório de interesse.
```bash
git clone https://github.com/dhruvvyas90/qemu-rpi-kernel.git
```

Por fim, execute o seguinte comando para emular, substituindo o PATH para os arquivos onde necessário:
```bash
qemu-system-arm \
  -kernel <path-to-qemu-kernel> \
  -cpu arm1176 \
  -m 256 \
  -M versatilepb \
  -serial stdio \
  -append "root=/dev/sda2 rootfstype=ext4 rw" \
  -hda <path-to-raspbian-img> \
  -no-reboot \
  -dtb <path-to-dtb-file> \
  -net user,hostfwd=tcp::2222-:22 \
  -net nic
```

Agora, em outra janela de terminal, basta se conectar à VM por SSH na porta especificada:
```bash
ssh -p 2222 pi@localhost
```

# Dependências
- QEMU
- GitPython
