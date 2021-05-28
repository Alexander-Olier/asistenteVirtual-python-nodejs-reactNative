import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack'


//Importando screens
import ChatScreen from './screens/chatScreen'

const AppNavigator = createStackNavigator(
  {
    Chat: ChatScreen
  },
  {
    headerMode:"none"
  }
)




export default createAppContainer(AppNavigator)