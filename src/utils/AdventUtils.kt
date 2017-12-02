/*
 * Kotlin implementations of Advent of Code problems' solutions,
 * written while learning Kotlin.
 *
 * Author: Adrian Kepka <kepka.adrian@gmail.com>
 *         https://github.com/Strus
 */

package utils

import java.io.File

class AdventUtils {
    companion object {
        fun getInputAsString(filename: String): String = File(filename).readText()
        fun getInputAsList(filename: String): List<String> = File(filename).readLines()
    }
}