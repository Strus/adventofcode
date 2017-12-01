package utils

import java.io.File

class AdventUtils {
    companion object {
        fun getInputAsString(filename: String): String = File(filename).readText()
        fun getInputAsList(filename: String): List<String> = File(filename).readLines()
    }
}