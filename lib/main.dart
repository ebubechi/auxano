import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'providers/wallet_provider.dart';
import 'package:auxano/utils/routes.dart';
import 'package:auxano/pages/login_page.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Load the private key
  WalletProvider walletProvider = WalletProvider();
  await walletProvider.loadPrivateKey();

  runApp(
    ChangeNotifierProvider<WalletProvider>.value(
      value: walletProvider,
      child: const MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      darkTheme: ThemeData.dark(),
      theme: ThemeData(
        useMaterial3: true
      ),
      initialRoute: MyRoutes.loginRoute,
      routes: {
        MyRoutes.loginRoute: (context) => const LoginPage(),
      },
    );
  }
}
