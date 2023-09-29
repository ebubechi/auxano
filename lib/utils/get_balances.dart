import 'package:auxano/constants/contants.dart';
import 'package:http/http.dart' as http;

Future<String> getBalances(String address, String chain) async {
  final url = Uri.http(uri, '/get-token-balance', {
    'address': address,
    'chain': chain,
  });

  final response = await http.get(url);

  if (response.statusCode == 200) {
    return response.body;
  } else {
    throw Exception('Failed to get balances');
  }
}