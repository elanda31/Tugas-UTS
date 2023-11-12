<?php
function caesarDecrypt($cipherText, $shift) {
    $result = '';

    $cipherText = strtoupper($cipherText);

    for ($i = 0; $i < strlen($cipherText); $i++) {
        if ($cipherText[$i] == ' ') {
            $result .= ' ';
        } else {
            $char = ord($cipherText[$i]) - $shift;
            if ($char < 65) {
                $char += 26;
            }
            $result .= chr($char);
        }
    }

    return $result;
}

// Contoh penggunaan:
$cipherText = "ELANDA RIK M";
$shift = 1;
$decryptedText = caesarDecrypt($cipherText, $shift);

echo "Teks Terenkripsi: $cipherText\n";
echo "Hasil Dekripsi: $decryptedText\n";
?>
